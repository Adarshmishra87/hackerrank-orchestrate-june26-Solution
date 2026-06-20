def decide_claim(claim_context, evidence_result, risk_flags):
    if not evidence_result["met"]:
        return {
            "status": "not_enough_information",
            "justification": evidence_result["reason"],
            "supporting_images": [],
            "severity": "unknown"
        }

    if evidence_result["contradicted"]:
        return {
            "status": "contradicted",
            "justification": evidence_result["reason"],
            "supporting_images": evidence_result["supporting_images"],
            "severity": "low"
        }

    severity_map = {
        "scratch": "low", "dent": "medium", "crack": "medium",
        "glass_shatter": "high", "broken_part": "medium",
        "stain": "medium", "water_damage": "medium"
    }
    severity = severity_map.get(claim_context["issue_type"], "unknown")

    return {
        "status": "supported",
        "justification": evidence_result["reason"],
        "supporting_images": evidence_result["supporting_images"],
        "severity": severity
    }
