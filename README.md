# Introduction to FastAPI

## Step 1: Project Setup

1. Create a GitHub repository.
2. Create a virtual environment using the `uv` package manager.
3. Install FastAPI.
4. Install Uvicorn with standard dependencies.

```bash
uv init fastapi-tutorial
cd fastapi-tutorial
uv add fastapi "uvicorn[standard]"
```

## Step 2: Create `main.py`

Create a file named `main.py` and add a GET endpoint.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Tutorial"}
```

## Step 3: Run the Server

Run the FastAPI application using Uvicorn:

```bash
uv run uvicorn main:app --reload
```

Open the following URLs in your browser:

- Application: http://127.0.0.1:8000/
- Interactive API documentation: http://127.0.0.1:8000/docs

### Common Uvicorn Commands

- `--host`: Specifies the network interface address to bind to.
- `--port`: Specifies the port number. The default is `8000`.
- `--reload`: Automatically restarts the server when code changes during development.
- `--version`: Displays the installed Uvicorn version.
- `--help`: Displays available commands and options.

Example:

```bash
uv run uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## Starting Uvicorn from Python Code

You can also start the server programmatically.

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
```

Run the program with:

```bash
python main.py
```

## Path Parameters

Path parameters are values passed directly through a URL path.

Example URL:

```text
http://localhost:8000/hello/sejal
```

Endpoint:

```python
@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}
```

Here, `name` is a path parameter. If the URL contains `/hello/sejal`, the value of `name` is `"sejal"`.

## HTTP Methods

### GET
Retrieves data from the server. It is commonly used to read information.

### POST
Sends data to the server, often to create a new resource.

### PUT
Replaces an existing resource with the supplied representation.

### PATCH
Updates part of an existing resource.

### DELETE
Requests the removal of a resource.

**Soft delete example:** In some applications, deleting an employee does not permanently remove the database record. Instead, the backend changes a field such as `is_active` from `True` to `False`. This is called a soft delete or logical delete.

For example, when employee Sejal is deleted, the application may mark her employee record as inactive.

## Async Keyword

The `async` keyword defines an asynchronous function in Python.

Example:

```python
@app.get("/async-example")
async def async_example():
    return {"message": "Hello from an async endpoint"}
```

Asynchronous functions can allow other work to proceed while waiting for supported I/O operations, such as network or database operations.

**Important:** Using `async` does not automatically make every function faster. Normal `def` functions are also valid in FastAPI.

FastAPI automatically converts returned dictionaries and other supported values into JSON responses. Pydantic models are commonly used to validate request data and define response structures, but they do not require the use of `async`.

## Parameter Validation

FastAPI supports validation for path parameters, query parameters and request bodies.

To validate path parameters, import `Path` from FastAPI.

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/hello/{name}")
def hello(
    name: str = Path(..., min_length=3, max_length=10)
):
    return {"name": name}
```

Here:

- `...` means the parameter is required.
- `min_length=3` requires at least three characters.
- `max_length=10` allows at most ten characters.

### Common Numeric Validation Rules

| Rule | Meaning |
|---|---|
| `gt=0` | Greater than zero |
| `ge=0` | Greater than or equal to zero |
| `lt=100` | Less than 100 |
| `le=100` | Less than or equal to 100 |

Example:

```python
from fastapi import Path

@app.get("/students/{student_id}")
def get_student(
    student_id: int = Path(..., ge=1, le=1000)
):
    return {"student_id": student_id}
```

The `student_id` must be an integer between 1 and 1000, inclusive.

Query parameters can also be validated using `Query`.

```python
from fastapi import Query

@app.get("/search")
def search(
    name: str = Query(..., min_length=3, max_length=20)
):
    return {"name": name}
```

Example URL:

```text
http://localhost:8000/search?name=Sejal
```

## Summary

In this introduction, we covered:

- Setting up a FastAPI project with `uv`.
- Creating GET endpoints.
- Running the application using Uvicorn.
- Starting Uvicorn programmatically.
- Understanding path parameters.
- Understanding GET, POST, PUT, PATCH and DELETE.
- Using asynchronous functions.
- Validating path and query parameters.
