from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository:
    def __init__(self, database: Session):
        self.database = database

    def list(self):
        return self.database.query(Task).order_by(Task.id.desc()).all()

    def find_by_id(self, task_id: int):
        return self.database.query(Task).filter(Task.id == task_id).first()

    def create(self, data: TaskCreate):
        task = Task(
            title=data.title,
            description=data.description
        )

        self.database.add(task)
        self.database.commit()
        self.database.refresh(task)

        return task

    def update(self, task: Task, data: TaskUpdate):
        payload = data.model_dump(exclude_unset=True)

        for field, value in payload.items():
            setattr(task, field, value)

        self.database.commit()
        self.database.refresh(task)

        return task

    def delete(self, task: Task):
        self.database.delete(task)
        self.database.commit()