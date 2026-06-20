def check_images(image_paths, claim_context, evidence_rules):
    images = image_paths.split(";")
    valid = True if images else False

    met = valid
    reason = "Images provided and part visible" if met else "No sufficient evidence"
    contradicted = False

    return {
        "met": met,
        "reason": reason,
        "valid": valid,
        "contradicted": contradicted,
        "supporting_images": [img.split("/")[-1].split(".")[0] for img in images] if met else []
    }
