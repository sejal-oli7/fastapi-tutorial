
# FastAPI Assignment 01

## Overview

This assignment covers the fundamental concepts of FastAPI,
including HTTP methods, path parameters, query parameters,
parameter validation, and Pydantic models.

## Topics Covered

1. Path Parameters
2. GET Request
3. POST Request
4. PUT Request
5. PATCH Request
6. DELETE Request
7. Query Parameters
8. Parameter Validation
9. Pydantic Models
10. Automatic API Documentation

## Project Structure

```text
fastapi-tutorial/
├── main.py
└── assignments/
    └── assignment_01/
        ├── main.py
        └── README.md
```

## Requirements

- Python
- FastAPI
- Uvicorn
- Pydantic

## Installation

Activate the existing virtual environment from the
fastapi-tutorial project root:

```bash
source .venv/bin/activate
```

Install the required packages if necessary:

```bash
pip install fastapi uvicorn
```

## Run the Application

Run this command from the fastapi-tutorial root directory:

```bash
uvicorn assignments.assignment_01.main:app --reload
```

## API Documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Alternative documentation:

http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | Welcome message |
| GET | /students | List all students |
| GET | /students/{student_id} | Get a student |
| POST | /students/{student_id} | Create a student |
| PUT | /students/{student_id} | Replace student data |
| PATCH | /students/{student_id} | Update selected fields |
| DELETE | /students/{student_id} | Delete a student |
| GET | /search?course=BCA&limit=5 | Search students |

## Example POST Request

Endpoint:

POST /students/2

Request body:

```json
{
  "name": "Sejal",
  "age": 20,
  "course": "BCA"
}
```

## Example PATCH Request

Endpoint:

PATCH /students/1

Request body:

```json
{
  "name": "Sejal Oli"
}
```

## Example Query Parameters

```text
/search?course=BCA&limit=5
```

- course: Filters students by course.
- limit: Controls the maximum number of returned results.

## Parameter Validation

- Student ID must be a positive integer.
- Student name must contain 2 to 50 characters.
- Student age must be between 16 and 100.
- Course name must contain at least 2 characters.
- Search limit must be between 1 and 100.

Invalid request data is automatically rejected by FastAPI.

## Pydantic Models

Pydantic BaseModel defines the expected structure of request data.

Field() adds validation rules to model fields.

model_dump() converts a Pydantic model into a Python dictionary.

## Important Note

This assignment uses temporary in-memory storage.
Data created during runtime is lost when the server restarts.

The project is intended for learning and practice.
It does not use a permanent database.
