def parse_claim(conversation, claim_object):
    issue_map = {
        "dent": "dent", "scratch": "scratch", "crack": "crack",
        "shatter": "glass_shatter", "broken": "broken_part",
        "missing": "missing_part", "torn": "torn_packaging",
        "crushed": "crushed_packaging", "water": "water_damage",
        "stain": "stain"
    }
    part_map = {
        "bumper": "rear_bumper" if "rear" in conversation else "front_bumper",
        "door": "door", "hood": "hood", "windshield": "windshield",
        "mirror": "side_mirror", "headlight": "headlight",
        "screen": "screen", "keyboard": "keyboard", "trackpad": "trackpad",
        "hinge": "hinge", "corner": "corner", "seal": "seal",
        "box": "box", "package": "package_side"
    }

    issue_type = "unknown"
    for k,v in issue_map.items():
        if k in conversation.lower():
            issue_type = v
            break

    object_part = "unknown"
    for k,v in part_map.items():
        if k in conversation.lower():
            object_part = v
            break

    return {"issue_type": issue_type, "object_part": object_part}
