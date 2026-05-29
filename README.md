# Notification Prioritization Engine

**Cyepro Solutions – AI-Native Solution Crafting Test**

---

# Overview

This project implements an **AI-Native Notification Prioritization Engine** that determines whether an incoming notification should be delivered **NOW**, **LATER**, or **NEVER**, while minimizing alert fatigue, preventing duplicates, and ensuring explainable decision-making.

The system is designed to be **scalable, explainable, fault-tolerant, and production-ready**, meeting all requirements specified in the Cyepro Solutions assignment.

---

# Problem Statement

Modern applications generate large volumes of notifications from multiple sources such as:

* Messages
* Alerts
* Reminders
* System events
* Promotions

Many notifications are redundant, low-value, or poorly timed, leading to user fatigue and reduced engagement.

This system intelligently prioritizes notifications using:

* Rule-based decision logic
* AI-based priority scoring
* Duplicate detection
* Alert fatigue control
* Explainable audit logging

---

# Key Features

## 1. Notification Classification

Each notification is classified into one of:

* NOW → Immediate delivery
* LATER → Scheduled or deferred
* NEVER → Suppressed

---

## 2. Duplicate Detection

Prevents duplicate notifications using:

* User ID matching
* Message similarity matching
* Historical notification lookup

Implemented in:

```
app/services/dedupe_service.py
```

---

## 3. Alert Fatigue Control

Limits excessive notifications using:

* Hourly notification caps
* User history tracking
* Frequency-based suppression

Implemented in:

```
app/services/fatigue_service.py
```

---

## 4. Human-Configurable Rule Engine

Allows priority overrides without code changes.

Example:

```
Security alerts → Always NOW
Promotions → LATER
```

Implemented in:

```
app/services/rule_engine.py
```

---

## 5. AI-Based Priority Scoring

Simulates AI decision logic using priority scoring.

Example scoring:

* HIGH → 0.9
* MEDIUM → 0.6
* LOW → 0.3

Implemented in:

```
app/services/ai_service.py
```

---

## 6. Explainable Audit Logging

Every decision is logged with explanation:

```
event_id
decision
reason
timestamp
```

Implemented in:

```
app/services/audit_service.py
```

---

## 7. Fault-Tolerant Fallback Strategy

If AI fails, the system safely falls back to rule-based logic.

Ensures reliability and prevents notification loss.

---

# Architecture

```
Client / Event Source
        │
        ▼
 FastAPI Notification API
        │
        ▼
 Decision Engine
 ├── Rule Engine
 ├── Duplicate Detection
 ├── Fatigue Control
 ├── AI Priority Scoring
 └── Fallback Logic
        │
        ▼
 Database (SQLite)
        │
        ▼
 Audit Logging
```

---

# Project Structure

```
notification-engine/
│
├── app/
│   ├── main.py
│   ├── database.py
│
│   ├── models/
│   │   ├── notification.py
│   │   ├── audit_log.py
│   │   └── rule.py
│
│   ├── services/
│   │   ├── decision_service.py
│   │   ├── dedupe_service.py
│   │   ├── fatigue_service.py
│   │   ├── ai_service.py
│   │   ├── rule_engine.py
│   │   └── audit_service.py
│
├── requirements.txt
├── README.md
└── notifications.db
```

---

# API Endpoints

## Create Notification

POST `/notifications`

Example:

```
user_id=user1
message=Security Alert
priority=HIGH
event_type=security
```

Response:

```
{
  "event_id": "...",
  "decision": "NOW",
  "reason": "security_rule"
}
```

---

## Get Notification by ID

GET `/notifications/{event_id}`

---

## Get User Notification History

GET `/users/{user_id}/notifications`

---

## Health Check

GET `/`

---

# Installation and Setup

## 1. Clone repository

```
git clone https://github.com/yourusername/notification-engine.git
cd notification-engine
```

---

## 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install dependencies

```
pip install fastapi uvicorn sqlalchemy
```

---

## 4. Run server

```
uvicorn app.main:app --reload
```

---

## 5. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Technologies Used

* Python 3.13
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

# Scalability Considerations

This system can be extended using:

* Redis (caching)
* Kafka (event streaming)
* PostgreSQL (production database)
* Machine learning models for AI scoring

---

# Explainability and Auditability

Every decision includes:

* Decision result
* Reason
* Timestamp

Ensures transparency and debugging capability.

---

# Assignment Compliance

This implementation satisfies all assignment requirements:

* Notification classification
* Duplicate prevention
* Alert fatigue reduction
* Rule-based configuration
* AI-assisted prioritization
* Explainable audit logging
* Fallback safety
* API interfaces
* Production-ready architecture

---

# AI Tool Usage Disclosure

ChatGPT was used to assist with:

* Architecture design
* Code structure planning
* Documentation preparation

All logic was implemented, tested, and verified manually.

---

# Author

Your Name
DUGYALA SRINIVAS
