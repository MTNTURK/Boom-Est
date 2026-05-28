"""
EST 4 Estimator — Claude AI plan analysis & estimate generation
"""
import anthropic
import base64
import json
import os
from pricing_data import DIVISIONS, GC_OVERHEAD_PROFIT_PCT, CONTINGENCY_PCT, STANDARD_EXCLUSIONS


def encode_file(file_path: str) -> tuple[str, str]:
    """Encode a file to base64 and detect its media type."""
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


def build_pricing_context() -> str:
    """Build a compact pricing reference from EST 4 data."""
    lines = ["EST 4 NYC COMMERCIAL INTERIOR PRICING REFERENCE (Union Labor, 2025-2026)\n"]
    for div_code, div in DIVISIONS.items():
        lines.append(f"\nDIVISION {div_code} — {div['name']}")
        for item in div["items"]:
            lines.append(
                f"  {item['code']} | {item['description']} | {item['uom']} | "
                f"Low: ${item['unit_low']:,.2f} | High: ${item['unit_high']:,.2f}"
            )
    lines.append(f"\nGC Overhead & Profit: {GC_OVERHEAD_PROFIT_PCT*100:.0f}%")
    lines.append(f"Design/Bid Contingency: {CONTINGENCY_PCT*100:.0f}%")
    return "\n".join(lines)


def analyze_plans(file_paths: list[str], project_info: dict) -> dict:
    """
    Send uploaded plans to Claude and get back a structured estimate.
    Returns a dict with line items, division subtotals, and summary.
    """
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    pricing_context = build_pricing_context()

    system_prompt = f"""You are EST 4, an expert NYC commercial interior construction estimator with 20+ years experience in Class A office tenant improvements, retail, and institutional spaces. You specialize in NYC union labor pricing.

Your job: analyze uploaded construction plans/documents and produce a detailed construction cost estimate in the EST 4 format.

{pricing_context}

INSTRUCTIONS:
1. Carefully review all uploaded plan documents
2. Identify every scope item visible in the plans
3. Map each item to the appropriate CSI division from the pricing reference above
4. Estimate realistic quantities based on what you can read from the plans
5. Use the Low/High unit rates from the pricing reference
6. If a scope item isn't in the reference, use your NYC union labor expertise to price it
7. Include ONLY divisions that have actual work items visible in the plans
8. Be specific — call out exact room names, dimensions, quantities when visible

OUTPUT FORMAT — Return ONLY valid JSON with this exact structure:
{{
  "project": {{
    "name": "Project name from plans",
    "address": "Address if visible",
    "client": "Client/owner if visible",
    "architect": "Architect if visible",
    "floor_area_sf": 0,
    "scope_summary": "2-3 sentence plain English scope description",
    "estimate_notes": "Any important assumptions or caveats"
  }},
  "divisions": [
    {{
      "code": "01",
      "name": "General Conditions & Requirements",
      "items": [
        {{
          "ref": "01.01",
          "description": "GC Project Management & Superintendent (est. X-Y wk duration)",
          "uom": "WKS",
          "qty": 10,
          "unit_low": 4500,
          "unit_high": 6000,
          "total_low": 45000,
          "total_high": 60000
        }}
      ],
      "subtotal_low": 0,
      "subtotal_high": 0
    }}
  ],
  "summary": {{
    "direct_cost_low": 0,
    "direct_cost_high": 0,
    "gc_overhead_profit_pct": 12,
    "gc_overhead_profit_low": 0,
    "gc_overhead_profit_high": 0,
    "contingency_pct": 5,
    "contingency_low": 0,
    "contingency_high": 0,
    "total_low": 0,
    "total_high": 0,
    "total_mid": 0,
    "cost_per_sf_low": 0,
    "cost_per_sf_high": 0,
    "cost_per_sf_mid": 0
  }},
  "scope_of_work": [
    {{
      "ref": "GC-1",
      "trade": "General Contractor",
      "description": "Detailed scope description...",
      "plans_ref": "Drawing sheet reference if visible"
    }}
  ],
  "exclusions": [
    "Item excluded from this estimate"
  ]
}}

CRITICAL: Return ONLY the JSON object. No markdown, no explanations, no code blocks. Pure JSON only."""

    # Build message content with all uploaded files
    content = []

    for file_path in file_paths:
        ext = os.path.splitext(file_path)[1].lower()
        if ext in [".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp"]:
            data, media_type = encode_file(file_path)
            if ext == ".pdf":
                content.append({
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": data,
                    }
                })
            else:
                content.append({
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": data,
                    }
                })
        elif ext in [".txt", ".md", ".csv"]:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            content.append({"type": "text", "text": f"[Document: {os.path.basename(file_path)}]\n{text}"})

    # Add project context if provided
    project_text = "Analyze these construction plans and generate a complete EST 4 construction cost estimate."
    if project_info.get("name"):
        project_text += f"\nProject name: {project_info['name']}"
    if project_info.get("address"):
        project_text += f"\nAddress: {project_info['address']}"
    if project_info.get("notes"):
        project_text += f"\nAdditional notes from submitter: {project_info['notes']}"

    content.append({"type": "text", "text": project_text})

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=8192,
        system=system_prompt,
        messages=[{"role": "user", "content": content}]
    )

    raw = response.content[0].text.strip()

    # Strip markdown code blocks if Claude wrapped it anyway
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    estimate = json.loads(raw)

    # Add standard exclusions if not already provided
    if not estimate.get("exclusions"):
        estimate["exclusions"] = STANDARD_EXCLUSIONS

    return estimate
