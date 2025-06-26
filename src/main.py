from typing import List

from fastapi import FastAPI, HTTPException
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel


class Student(BaseModel):
    student_id: int
    name: str
    utme_score: int
    subjects: List[str]


STUDENTS_DB = {
    1: Student(
        student_id=1,
        name="Chinedu Obi",
        utme_score=285,
        subjects=["Mathematics", "Physics", "Chemistry"],
    ),
    2: Student(
        student_id=2,
        name="Fatima Yusuf",
        utme_score=310,
        subjects=["Government", "Economics", "Literature"],
    ),
    3: Student(
        student_id=3,
        name="Tunde Adebayo",
        utme_score=250,
        subjects=["Mathematics", "Economics", "Geography"],
    ),
}

app = FastAPI(
    title="UTME Prep API",
    description="API for accessing student data and past questions for the UTME exam.",
)


@app.get("/students/{student_id}", operation_id="get_student_by_id")
async def get_student_by_id(student_id: int) -> Student:
    """
    Retrieves a student's profile by their unique ID.
    """
    student = STUDENTS_DB.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/subjects", operation_id="get_all_subjects")
async def get_all_subjects():
    """
    Returns a list of all available subjects in the database.
    """
    all_subjects = set()
    for student in STUDENTS_DB.values():
        all_subjects.update(student.subjects)
    return {"subjects": sorted(list(all_subjects))}


mcp_server = FastApiMCP(
    app,
    name="UTME Prep Assistant",
    description="A tool for an AI agent to interact with UTME student data.",
    describe_full_response_schema=True,  # Describe the full response JSON-schema instead of just a response example
    describe_all_responses=True,  # Describe all the possible responses instead of just the success (2XX) response
)
mcp_server.mount()
