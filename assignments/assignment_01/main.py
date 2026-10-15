
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI Assignment 01",
    description="Practice Path Parameters, Query Parameters, Validation and Pydantic Models",
    version="1.0.0"
)


# ==========================================
# 1. PYDANTIC MODELS
# ==========================================

class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=16, le=100)
    course: str = Field(min_length=2)


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    age: int | None = Field(default=None, ge=16, le=100)
    course: str | None = Field(default=None, min_length=2)


# ==========================================
# 2. TEMPORARY DATA
# ==========================================

students = {
    1: {
        "name": "Ram",
        "age": 20,
        "course": "BCA"
    }
}


# ==========================================
# 3. HOME ROUTE
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Assignment 01"
    }


# ==========================================
# 4. GET - READ STUDENT
# ==========================================

@app.get("/students/{student_id}")
def get_student(
    student_id: int = Path(
        gt=0,
        description="Student ID must be positive"
    )
):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student_id": student_id,
        **students[student_id]
    }


# ==========================================
# 5. POST - CREATE STUDENT
# ==========================================

@app.post("/students/{student_id}", status_code=201)
def create_student(
    student_id: int,
    student: Student
):
    if student_id <= 0:
        raise HTTPException(
            status_code=422,
            detail="Student ID must be positive"
        )

    if student_id in students:
        raise HTTPException(
            status_code=409,
            detail="Student already exists"
        )

    students[student_id] = student.model_dump()

    return {
        "message": "Student created successfully",
        "student_id": student_id,
        "data": students[student_id]
    }


# ==========================================
# 6. PUT - REPLACE STUDENT DATA
# ==========================================

@app.put("/students/{student_id}")
def replace_student(
    student_id: int,
    student: Student
):
    if student_id <= 0:
        raise HTTPException(
            status_code=422,
            detail="Student ID must be positive"
        )

    students[student_id] = student.model_dump()

    return {
        "message": "Student replaced successfully",
        "student_id": student_id,
        "data": students[student_id]
    }


# ==========================================
# 7. PATCH - UPDATE SELECTED FIELDS
# ==========================================

@app.patch("/students/{student_id}")
def update_student(
    student_id: int,
    student: StudentUpdate
):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = student.model_dump(exclude_unset=True)

    students[student_id].update(update_data)

    return {
        "message": "Student updated successfully",
        "student_id": student_id,
        "data": students[student_id]
    }


# ==========================================
# 8. DELETE - REMOVE STUDENT
# ==========================================

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "data": deleted_student
    }


# ==========================================
# 9. QUERY PARAMETERS + VALIDATION
# ==========================================

@app.get("/search")
def search_students(
    course: str = Query(
        min_length=2,
        description="Course name to search"
    ),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Maximum number of results"
    )
):
    results = [
        {
            "student_id": student_id,
            **student
        }
        for student_id, student in students.items()
        if student["course"].lower() == course.lower()
    ]

    return {
        "course": course,
        "limit": limit,
        "total_found": len(results),
        "results": results[:limit]
    }


# ==========================================
# 10. GET - LIST ALL STUDENTS
# ==========================================

@app.get("/students")
def list_students():
    return {
        "total_students": len(students),
        "students": students
    }
