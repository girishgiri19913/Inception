from fastapi import FastAPI
import models
from database import engine
from routers import create_project, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(create_project.router)
# app.include_router(todos.router)
