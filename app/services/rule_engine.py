def apply_rules(event):
    """
    Human-configurable rules engine
    """

    # Example rules (can be moved to database later)

    if event.event_type == "security":
        return "NOW", "security_rule"

    if event.event_type == "system":
        return "NOW", "system_rule"

    if event.event_type == "promotion":
        return "LATER", "promotion_rule"

    return None, None