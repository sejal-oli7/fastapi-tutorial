# FastAPI Tutorial

A beginner-friendly FastAPI practice project covering API endpoints, path parameters, query parameters, validation, and Pydantic models.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

```text
fastapi-tutorial/
├── main.py
├── README.md
└── assignments/
    └── assignment_01/
        ├── main.py
        └── README.md
```

## Setup and Installation

Clone the repository:

```bash
git clone https://github.com/sejal-oli7/fastapi-tutorial.git
cd fastapi-tutorial
```

Install dependencies:

```bash
uv sync
```

If `uv sync` reports that the project dependencies are not configured, install them with:

```bash
uv add fastapi "uvicorn[standard]"
```

## Run the Main Tutorial

```bash
uv run uvicorn main:app --reload --port 8000
```

Open the interactive API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display the welcome message |
| GET | `/greet/{name}` | Greet a person by name |
| POST | `/add_students` | Add a student using request parameters |
| GET | `/get_students` | Retrieve the student list |
| GET | `/hey` | Practice query parameters |
| GET | `/hello/{name}` | Validate a name path parameter |
| GET | `/hello/{name}/{age}` | Validate name and age |
| POST | `/students` | Receive student data using a Pydantic model |
| POST | `/blog` | Receive blog post data |
| POST | `/student_profile` | Receive a complete student profile |

## Example Requests

### 1. Greet a Person

```http
GET /greet/Sejal
```

### 2. Add a Student

The `/add_students` endpoint receives `name`, `age`, and `course` as request parameters.

Example:

```http
POST /add_students?name=Sejal&age=21&course=BCA
```

### 3. Create a Student

Send a JSON request body to `POST /students`:

```json
{
  "id": 1,
  "name": "Sejal",
  "subjects": ["Machine Learning", "FastAPI", "Python"]
}
```

### 4. Create a Blog Post

Send a JSON request body to `POST /blog`:

```json
{
  "title": "Introduction to FastAPI",
  "content": "FastAPI is a Python framework for building APIs."
}
```

### 5. Create a Student Profile

Send a JSON request body to `POST /student_profile`:

```json
{
  "name": "Sejal Oli",
  "phone": "9800000000",
  "address": "Chitwan, Nepal",
  "college_name": "Oxford College of Engineering and Management",
  "email": "olisejal67@gmail.com",
  "faculty": "BCA",
  "subjects": ["Python", "Machine Learning", "FastAPI"],
  "marks": [85, 90, 88]
}
```

## Concepts Practiced

- GET and POST HTTP methods
- Path parameters
- Query parameters
- Parameter validation using `Path`
- Pydantic `BaseModel`
- Request body validation
- Python type hints
- Basic API development with FastAPI

## Note

This is a learning project. Student records added through the in-memory `students` list are not stored in a database and are reset when the application restarts.

The `/students` and `/blog` endpoints demonstrate Pydantic models, while `/student_profile` validates and receives student profile data.

## Assignment

See [`assignments/assignment_01/README.md`](assignments/assignment_01/README.md) for the separate Assignment 01 documentation.
