"""
EST 4 Estimator — Claude AI plan analysis & estimate generation
"""
import anthropic
import base64
import json
import os
from pricing_data import DIVISIONS, GC_OVERHEAD_PROFIT_PCT, CONTINGENCY_PCT, STANDARD_EXCLUSIONS


def encode_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    media_map = {
        ".pdf": "application/pdf",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    media_type = media_map.get(ext, "application/octet-stream")
    with open(file_path, "rb") as f:
        data = base64.standard_b64encode(f.read()).decode("utf-8")
    return data, media_type


def analyze_plans(file_paths, project_info):
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

    content = []
    MAX_BYTES = 4 * 1024 * 1024

    for file_path in file_paths:
        ext = os.path.splitext(file_path)[1].lower()
        size = os.path.getsize(file_path)
        if ext in [".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp"]:
            if size > MAX_BYTES:
                content.append({"type": "text", "text": f"File too large: {os.path.basename(file_path)}. Add scope notes manually."})
                continue
            data, media_type = encode_file(file_path)
            if ext == ".pdf":
                content.append({"type": "document", "source": {"type": "base64", "media_type": media_type, "data": data}})
            else:
                content.append({"type": "image", "source": {"type": "base64", "media_type": media_type, "data": data}})
        elif ext in [".txt", ".md", ".csv", ".docx"]:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read(50000)
            content.append({"type": "text", "text": f"[Document: {os.path.basename(file_path)}]\n{text}"})

    project_text = "Analyze these construction plans and generate a complete NYC union labor construction cost estimate."
    if project_info.get("name"):
        project_text += f"\nProject: {project_info['name']}"
    if project_info.get("notes"):
        project_text += f"\nNotes: {project_info['notes']}"
    content.append({"type": "text", "text": project_text})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system="""You are an expert NYC commercial construction estimator. Analyze the uploaded plans and return a JSON estimate with this structure:
{"project":{"name":"","address":"","floor_area_sf":0,"scope_summary":""},"divisions":[{"code":"01","name":"General Conditions","items":[{"ref":"01.01","description":"","uom":"LS","qty":1,"unit_low":0,"unit_high":0,"total_low":0,"total_high":0}],"subtotal_low":0,"subtotal_high":0}],"summary":{"direct_cost_low":0,"direct_cost_high":0,"gc_overhead_profit_pct":12,"gc_overhead_profit_low":0,"gc_overhead_profit_high":0,"contingency_pct":5,"contingency_low":0,"contingency_high":0,"total_low":0,"total_high":0,"total_mid":0,"cost_per_sf_low":0,"cost_per_sf_high":0,"cost_per_sf_mid":0},"scope_of_work":[{"ref":"","trade":"","description":""}],"exclusions":[]}
Return ONLY valid JSON. No markdown.""",
        messages=[{"role": "user", "content": content}]
    )

    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    estimate = json.loads(raw)
    if not estimate.get("exclusions"):
        estimate["exclusions"] = ["Permits and filing fees", "Asbestos/hazmat abatement", "Structural work", "MEP engineering fees"]
    return estimate
