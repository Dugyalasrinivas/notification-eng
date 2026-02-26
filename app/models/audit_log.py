from sqlalchemy import Column, String, DateTime
from datetime import datetime
from ..database import Base

class AuditLog(Base):

    __tablename__ = "audit_logs"

    log_id = Column(String, primary_key=True)
    event_id = Column(String)
    decision = Column(String)
    reason = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)