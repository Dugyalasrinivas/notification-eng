from .rule_engine import apply_rules
from .ai_service import get_priority_score
from .dedupe_service import is_duplicate
from .fatigue_service import is_fatigued

def decide_notification(db, event):
    """
    Main decision engine that determines NOW / LATER / NEVER
    """

    # Step 1: Apply human-configurable rules
    decision, reason = apply_rules(event)

    if decision:
        return decision, reason

    # Step 2: Duplicate detection
    if is_duplicate(db, event):
        return "NEVER", "duplicate_detected"

    # Step 3: Fatigue control
    if is_fatigued(db, event):
        return "LATER", "fatigue_limit_reached"

    # Step 4: AI priority scoring
    try:
        score = get_priority_score(event.priority)
    except Exception:
        # Fallback if AI fails
        score = 0.5
        return "LATER", "ai_fallback"

    if score >= 0.8:
        return "NOW", "ai_high_priority"

    if score >= 0.5:
        return "LATER", "ai_medium_priority"

    return "NEVER", "ai_low_priority"