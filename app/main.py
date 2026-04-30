from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routers.task_router import router as task_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todolist API")

app.include_router(task_router)


@app.get("/")
def health_check():
    return {"message": "Todolist API rodando"}