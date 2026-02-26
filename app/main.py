import uuid
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Database
from app.database import SessionLocal, engine, Base

# Models
from app.models.notification import Notification

# Services
from app.services.decision_service import decide_notification
from app.services.audit_service import log_decision


# Create database tables
Base.metadata.create_all(bind=engine)


# Initialize FastAPI
app = FastAPI(
    title="Notification Prioritization Engine",
    description="AI-powered notification decision system (Now / Later / Never)",
    version="1.0"
)


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Root endpoint
@app.get("/")
def root():
    return {
        "status": "running",
        "service": "Notification Prioritization Engine"
    }


# Create notification endpoint
@app.post("/notifications")
def create_notification(
    user_id: str,
    message: str,
    priority: str,
    event_type: str = "default",
    db: Session = Depends(get_db)
):

    # Generate unique event id
    event_id = str(uuid.uuid4())

    # Create event object
    class Event:
        pass

    event = Event()
    event.event_id = event_id
    event.user_id = user_id
    event.message = message
    event.priority = priority
    event.event_type = event_type

    # Decision engine
    decision, reason = decide_notification(db, event)

    # Audit log (assignment requirement)
    log_decision(event_id, decision, reason)

    # Save notification in database
    notification = Notification(
        event_id=event_id,
        user_id=user_id,
        event_type=event_type,
        message=message,
        priority=priority,
        decision=decision
    )

    db.add(notification)
    db.commit()

    return {
        "event_id": event_id,
        "decision": decision,
        "reason": reason,
        "status": "processed"
    }


# Get all notifications for a user
@app.get("/users/{user_id}/notifications")
def get_user_notifications(user_id: str, db: Session = Depends(get_db)):

    notifications = db.query(Notification).filter(
        Notification.user_id == user_id
    ).all()

    return {
        "count": len(notifications),
        "notifications": notifications
    }


# Get specific notification by event id
@app.get("/notifications/{event_id}")
def get_notification(event_id: str, db: Session = Depends(get_db)):

    notification = db.query(Notification).filter(
        Notification.event_id == event_id
    ).first()

    if not notification:
        return {
            "error": "Notification not found"
        }

    return notification