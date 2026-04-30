from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, database: Session):
        self.repository = TaskRepository(database)

    def list_tasks(self):
        return self.repository.list()

    def get_task(self, task_id: int):
        task = self.repository.find_by_id(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")

        return task

    def create_task(self, data: TaskCreate):
        return self.repository.create(data)

    def update_task(self, task_id: int, data: TaskUpdate):
        task = self.get_task(task_id)

        return self.repository.update(task, data)

    def delete_task(self, task_id: int):
        task = self.get_task(task_id)

        self.repository.delete(task)

        return {"message": "Tarefa removida com sucesso"}