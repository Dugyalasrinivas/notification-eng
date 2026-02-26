from sqlalchemy.orm import Session
from ..models.notification import Notification

def is_duplicate(db: Session, event):
    """
    Check if notification is duplicate
    """

    existing = db.query(Notification).filter(
        Notification.user_id == event.user_id,
        Notification.message == event.message
    ).first()

    if existing:
        return True

    return False