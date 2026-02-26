from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..models.notification import Notification

MAX_NOTIFICATIONS_PER_HOUR = 5

def is_fatigued(db: Session, event):
    """
    Check if user received too many notifications recently
    """

    one_hour_ago = datetime.utcnow() - timedelta(hours=1)

    count = db.query(Notification).filter(
        Notification.user_id == event.user_id,
        Notification.created_at >= one_hour_ago
    ).count()

    if count >= MAX_NOTIFICATIONS_PER_HOUR:
        return True

    return False