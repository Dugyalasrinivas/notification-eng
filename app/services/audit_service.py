import uuid
from datetime import datetime

audit_logs = []

def log_decision(event_id, decision, reason):

    audit_logs.append({
        "log_id": str(uuid.uuid4()),
        "event_id": event_id,
        "decision": decision,
        "reason": reason,
        "timestamp": datetime.utcnow()
    })