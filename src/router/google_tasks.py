from fastapi import APIRouter
from googleapiclient.discovery import build

from src.schemas.google_tasks import TaskCreate, TaskDelete

router = APIRouter()


@router.post("/create", tags=["Google Tasks"])
def create_task(data: TaskCreate):
    service = build("tasks", "v1", credentials=data.get_credentials())
    task = (
        service.tasks()
        .insert(tasklist="@default", body={"title": data.task_title, "due": data.due})
        .execute()
    )
    return {"task_id": task.get("id")}


@router.post("/delete", tags=["Google Tasks"])
def delete_task(data: TaskDelete):
    service = build("tasks", "v1", credentials=data.get_credentials())
    service.tasks().delete(tasklist="@default", task=data.task_id).execute()
    return {"status": "deleted"}
