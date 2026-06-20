def analyze_risks(user_id, user_history, evidence_result):
    risks = []
    if not evidence_result["valid"]:
        risks.append("damage_not_visible")
    if user_id in user_history and user_history[user_id].get("rejected_claim", 0) > 3:
        risks.append("user_history_risk")
    return risks
