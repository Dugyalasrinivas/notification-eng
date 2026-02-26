from sqlalchemy import Column, String, DateTime
from datetime import datetime
from ..database import Base

class Notification(Base):

    __tablename__ = "notifications"

    event_id = Column(String, primary_key=True)
    user_id = Column(String)
    event_type = Column(String)
    message = Column(String)
    priority = Column(String)
    decision = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)