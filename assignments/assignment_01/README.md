# FastAPI Assignment 01

**Version:** 1.0.0

A FastAPI assignment for practicing path parameters, query parameters, request validation, Pydantic models, and CRUD operations.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

## Run the Assignment

From the root `fastapi-tutorial` directory, run:

```bash
uv run uvicorn --app-dir assignments/assignment_01 main:app --reload --port 8001
```

Open the API documentation:

- Swagger UI: http://127.0.0.1:8001/docs
- OpenAPI schema: http://127.0.0.1:8001/openapi.json

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display the welcome message |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| POST | `/students/{student_id}` | Create a new student |
| PUT | `/students/{student_id}` | Replace a student's data |
| PATCH | `/students/{student_id}` | Update selected student fields |
| DELETE | `/students/{student_id}` | Delete a student |
| GET | `/search?course=BCA&limit=10` | Search students by course |
| GET | `/students` | List all students |

## Student Pydantic Model

The `Student` model defines the required fields:

| Field | Type | Validation |
|---|---|---|
| `name` | String | 2–50 characters |
| `age` | Integer | 16–100 |
| `course` | String | At least 2 characters |

Example request body:

```json
{
  "name": "Sejal",
  "age": 21,
  "course": "BCA"
}
```

## Create a Student

Send a POST request to:

```http
POST /students/2
```

Request body:

```json
{
  "name": "Sejal",
  "age": 21,
  "course": "BCA"
}
```

The endpoint creates a student with ID `2`, provided that the ID does not already exist.

## Update a Student

### PUT

Send all required fields to replace a student's data:

```http
PUT /students/1
```

### PATCH

Send only the fields you want to update:

```http
PATCH /students/1
```

Example body:

```json
{
  "age": 22
}
```

## Search Students

Search for students enrolled in BCA:

```http
GET /search?course=BCA&limit=10
```

- `course` is a required query parameter with a minimum length of 2.
- `limit` is optional, defaults to 10, and must be between 1 and 100.

## Delete a Student

```http
DELETE /students/1
```

The endpoint removes the student if the ID exists.

## Concepts Practiced

- Path parameters using `Path`
- Query parameters using `Query`
- Request validation using Pydantic `Field`
- Pydantic models for request bodies
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- CRUD operations
- HTTP error responses, including 404 and 409

## Important Notes

- Student records are stored in a Python dictionary in memory, not in a database.
- The assignment starts with one sample student: ID `1`, name `Ram`, age `20`, course `BCA`.
- Changes are lost when the application restarts.
- PUT replaces the data for the specified ID and can create a record if that ID does not exist.
- PATCH updates the fields supplied in the request.
