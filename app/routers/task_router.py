from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_database
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=list[TaskResponse])
def list_tasks(database: Session = Depends(get_database)):
    service = TaskService(database)

    return service.list_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, database: Session = Depends(get_database)):
    service = TaskService(database)

    return service.get_task(task_id)


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate, database: Session = Depends(get_database)):
    service = TaskService(database)

    return service.create_task(data)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, database: Session = Depends(get_database)):
    service = TaskService(database)

    return service.update_task(task_id, data)


@router.delete("/{task_id}")
def delete_task(task_id: int, database: Session = Depends(get_database)):
    service = TaskService(database)

    return service.delete_task(task_id)