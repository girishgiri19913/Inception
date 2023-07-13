from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from starlette import status
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Project(BaseModel):
    project_name: str


@router.post("/create_project", status_code=status.HTTP_201_CREATED)
async def create_user(project: Project, db: Session = Depends(get_db)):
    print(project.project_name)
    project_model = models.Projects()
    project_model.project_name = project.project_name 
    db.add(project_model)
    db.commit()

    return 'Project created'

    