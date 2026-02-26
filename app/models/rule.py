from sqlalchemy import Column, String, Boolean
from ..database import Base

class Rule(Base):

    __tablename__ = "rules"

    rule_id = Column(String, primary_key=True)
    event_type = Column(String)
    decision = Column(String)
    enabled = Column(Boolean, default=True)