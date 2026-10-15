
# Import required modules
from fastapi import FastAPI, Path
from pydantic import BaseModel, ValidationError
from typing import List
import uvicorn

# Create a FastAPI instance
app = FastAPI()

# Store student details
students = []


# 1. GET endpoint: Home
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Tutorial"}


# 2. GET endpoint: Greet a person
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


# 3. POST endpoint: Add a student
@app.post("/add_students")
def add_students(name: str, age: int, course: str):
    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    return {
        "message": "Student added",
        "student": student
    }


# 4. GET endpoint: Get all students
@app.get("/get_students")
def get_students():
    return {"students": students}


# 5. GET endpoint: Query parameters
@app.get("/hey")
async def hey(name: str, age: int):
    return {"name": name, "age": age}


# 6. GET endpoint: Validate name length
@app.get("/hello/{name}")
async def hello_name(
    name: str = Path(..., min_length=3, max_length=10)
):
    return {"name": name}


# 7. GET endpoint: Validate name and age
@app.get("/hello/{name}/{age}")
async def hello_student(
    name: str = Path(..., min_length=3, max_length=10),
    age: int = Path(..., ge=1, le=100)
):
    return {"name": name, "age": age}


# 8. Pydantic model: Student
class Student(BaseModel):
    id: int
    name: str
    subjects: List[str] = []


# 9. Sample student data
data = {
    "id": 1,
    "name": "Sejal",
    "subjects": ["ML", "Full stack", "Web development"]
}


# 10. Create a Student object
s1 = Student(**data)


# 11. POST endpoint: Add student using Pydantic
@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student data received",
        "student": student.model_dump()
    }


# 12. Pydantic model: BlogPost
class BlogPost(BaseModel):
    title: str
    content: str


# 13. Validate BlogPost data in Python
try:
    post_data = BlogPost(
        title="Introduction to Pydantic",
        content="Pydantic is a Python library for data validation."
    )

    print("Valid blog post:")
    print(post_data)

    second_post = BlogPost(
        title="123",
        content="42"
    )

    print("Second blog post:")
    print(second_post)

except ValidationError as e:
    print("Validation error:", e)


# 14. POST endpoint: Create a blog post
@app.post("/blog")
def create_blog(post: BlogPost):
    return {
        "message": "Blog post received successfully",
        "blog": post.model_dump()
    }


# 15. Pydantic model: Student Profile
class StudentProfile(BaseModel):
    name: str
    phone: str
    address: str
    college_name: str
    email: str
    faculty: str
    subjects: List[str]
    marks: List[float]


# 16. POST endpoint: Create student profile
@app.post("/student_profile")
def student_profile(payload: StudentProfile):
    return {
        "message": "Student profile created successfully",
        "student_profile": payload.model_dump()
    }


# 17. Run the server
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
