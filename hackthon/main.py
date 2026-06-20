import pandas as pd
from modules.claim_parser import parse_claim
from modules.image_checker import check_images
from modules.risk_analyzer import analyze_risks
from modules.decision_engine import decide_claim

def process_claims(claims_file, user_history_file, evidence_file, output_file):
    claims = pd.read_csv(claims_file)
    user_history = pd.read_csv(user_history_file).set_index("user_id").to_dict("index")
    evidence_rules = pd.read_csv(evidence_file)

    results = []
    for _, row in claims.iterrows():
        claim_context = parse_claim(row["user_claim"], row["claim_object"])
        evidence_result = check_images(row["image_paths"], claim_context, evidence_rules)
        risk_flags = analyze_risks(row["user_id"], user_history, evidence_result)
        decision = decide_claim(claim_context, evidence_result, risk_flags)

        results.append({
            "user_id": row["user_id"],
            "image_paths": row["image_paths"],
            "user_claim": row["user_claim"],
            "claim_object": row["claim_object"],
            "evidence_standard_met": evidence_result["met"],
            "evidence_standard_met_reason": evidence_result["reason"],
            "risk_flags": ";".join(risk_flags) if risk_flags else "none",
            "issue_type": claim_context["issue_type"],
            "object_part": claim_context["object_part"],
            "claim_status": decision["status"],
            "claim_status_justification": decision["justification"],
            "supporting_image_ids": ";".join(decision["supporting_images"]) if decision["supporting_images"] else "none",
            "valid_image": str(evidence_result["valid"]).lower(),
            "severity": decision["severity"]
        })

    pd.DataFrame(results).to_csv(output_file, index=False)

if __name__ == "__main__":
    process_claims("dataset/claims.csv", "dataset/user_history.csv", "dataset/evidence_requirements.csv", "output.csv")
