# Incident Management System

## Overview

This project is a full-stack Incident Management System built using:

* FastAPI (Backend)
* MySQL (Database)
* HTML, CSS, JavaScript (Frontend)
* SQLAlchemy ORM

It allows users to:

* Create incidents
* View incidents
* Search incidents
* Filter incidents
* Update incident status
* Pagination and sorting

---

## Project Structure

```
incident-management-system/
│
├── backend/      # FastAPI backend
├── frontend/     # HTML, CSS, JS frontend
├── README.md
```

---

## Backend Setup Instructions

### Step 1: Go to backend folder

```
cd backend
```

### Step 2: Create virtual environment

```
python -m venv myenv
```

Activate:

Windows:

```
myenv\Scripts\activate
```

---

### Step 3: Install dependencies

```
pip install -r requirements.txt
```

---

### Step 4: Start FastAPI server

```
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup Instructions

Open frontend folder:

```
frontend/index.html
```

Double click to open in browser.

OR use Live Server in VS Code.

---

## API Overview

### Create Incident

POST `/api/incidents`

Request Body:

```
{
"title": "Server Down",
"service": "Payment Service",
"severity": "SEV1",
"status": "OPEN",
"owner": "Admin",
"summary": "Server not responding"
}
```

---

### Get Incidents

GET `/api/incidents`

Supports:

* pagination
* search
* filter
* sorting

Example:

```
/api/incidents?page=0&size=10&search=server
```

---

### Get Incident by ID

GET `/api/incidents/{id}`

---

### Update Incident Status

PATCH `/api/incidents/{id}`

---

## Design Decisions & Tradeoffs

Design decisions:

* Used FastAPI for fast backend development
* Used SQLAlchemy ORM for database abstraction
* Used MySQL for reliable relational database
* Used plain HTML/CSS/JS for simplicity

Tradeoffs:

* No authentication implemented
* No frontend framework used (React optional)

---

## Improvements with More Time

If more time available, I would add:

* Authentication (JWT)
* User login system
* Better frontend using React
* Docker containerization
* Unit testing
* Deployment on cloud (AWS)

---

## Author

Varun Valluri
