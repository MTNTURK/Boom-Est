"""
EST 4 Web Estimator — Flask Application
"""
import os
import uuid
import json
import traceback
from datetime import datetime
from flask import (Flask, render_template, request, redirect,
                   url_for, session, send_file, jsonify, flash)
from werkzeug.utils import secure_filename
from estimator import analyze_plans
from excel_output import generate_excel

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "est4-change-this-in-production")

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif", "webp", "txt", "docx"}
MAX_FILES = 10
MAX_FILE_MB = 50

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ── Pricing tier logic ──────────────────────────────────────────────────────────

PRICING = {
    "free_uses": 2,
    "use_3_price": 100,
    "use_4_price": 250,
    "monthly_per_project": 250,
    "annual_license": 19800,
    "annual_per_plan": 100,
    "monthly_flat": 1800,
}

def get_use_count():
    return session.get("use_count", 0)

def increment_use():
    session["use_count"] = session.get("use_count", 0) + 1
    return session["use_count"]

def is_paid_member():
    return session.get("paid_member", False)

def get_price_for_next_use():
    count = get_use_count()
    if count < PRICING["free_uses"]:
        return 0
    elif count == PRICING["free_uses"]:
        return PRICING["use_3_price"]
    elif count == PRICING["free_uses"] + 1:
        return PRICING["use_4_price"]
    else:
        return None  # Requires membership

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Routes ──────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    use_count = get_use_count()
    price = get_price_for_next_use()
    uses_remaining_free = max(0, PRICING["free_uses"] - use_count)
    return render_template("index.html",
                           use_count=use_count,
                           price=price,
                           uses_remaining_free=uses_remaining_free,
                           pricing=PRICING,
                           is_paid=is_paid_member())


@app.route("/analyze", methods=["POST"])
def analyze():
    use_count = get_use_count()
    price = get_price_for_next_use()

    # Check if user needs to pay and hasn't
    if price is None and not is_paid_member():
        return redirect(url_for("upgrade"))

    if price and price > 0 and not request.form.get("payment_confirmed"):
        # In production: integrate Stripe here before proceeding
        # For MVP: trust the confirmation checkbox
        pass

    # Collect uploaded files
    files = request.files.getlist("plans")
    if not files or all(f.filename == "" for f in files):
        flash("Please upload at least one plan file.", "error")
        return redirect(url_for("index"))

    session_id = str(uuid.uuid4())
    upload_dir = os.path.join(UPLOAD_FOLDER, session_id)
    os.makedirs(upload_dir)

    saved_paths = []
    for f in files[:MAX_FILES]:
        if f and f.filename and allowed_file(f.filename):
            fname = secure_filename(f.filename)
            fpath = os.path.join(upload_dir, fname)
            f.save(fpath)
            # Check file size
            if os.path.getsize(fpath) > MAX_FILE_MB * 1024 * 1024:
                os.remove(fpath)
                continue
            saved_paths.append(fpath)

    if not saved_paths:
        flash("No valid files were uploaded. Please use PDF, PNG, JPG, or similar.", "error")
        return redirect(url_for("index"))

    project_info = {
        "name": request.form.get("project_name", "").strip(),
        "address": request.form.get("project_address", "").strip(),
        "notes": request.form.get("notes", "").strip(),
    }

    try:
        # Run the estimate
        estimate = analyze_plans(saved_paths, project_info)

        # Save estimate JSON for the session
        estimate["_meta"] = {
            "session_id": session_id,
            "generated_at": datetime.now().isoformat(),
            "files_analyzed": [os.path.basename(p) for p in saved_paths],
        }

        estimate_path = os.path.join(OUTPUT_FOLDER, f"{session_id}_estimate.json")
        with open(estimate_path, "w") as f:
            json.dump(estimate, f, indent=2)

        # Generate Excel file
        project_name = estimate.get("project", {}).get("name", "Project")
        safe_name = secure_filename(project_name[:40])
        excel_filename = f"EST4_{safe_name}_{datetime.now().strftime('%Y%m%d')}.xlsx"
        excel_path = os.path.join(OUTPUT_FOLDER, f"{session_id}_{excel_filename}")
        generate_excel(estimate, excel_path)

        increment_use()

        return render_template("result.html",
                               estimate=estimate,
                               session_id=session_id,
                               excel_filename=excel_filename,
                               use_count=get_use_count(),
                               pricing=PRICING)

    except Exception as e:
        traceback.print_exc()
        flash(f"An error occurred while analyzing your plans: {str(e)}", "error")
        return redirect(url_for("index"))


@app.route("/download/<session_id>")
def download(session_id):
    """Download the generated Excel estimate."""
    # Find the Excel file for this session
    for fname in os.listdir(OUTPUT_FOLDER):
        if fname.startswith(session_id) and fname.endswith(".xlsx"):
            fpath = os.path.join(OUTPUT_FOLDER, fname)
            display_name = fname.replace(f"{session_id}_", "")
            return send_file(fpath, as_attachment=True, download_name=display_name)
    return "File not found", 404


@app.route("/upgrade")
def upgrade():
    return render_template("pricing.html", pricing=PRICING)


@app.route("/demo-paid")
def demo_paid():
    """Demo route — in production replace with real Stripe webhook."""
    session["paid_member"] = True
    flash("Membership activated! You now have unlimited access.", "success")
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "EST 4 Estimator"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
