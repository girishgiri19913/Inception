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

@router.get("/projects", status_code=status.HTTP_200_OK)
async def get_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Projects).all()
    return projects


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

@router.put("/update_project/{project_id}", status_code=status.HTTP_200_OK)
async def update_project(project_id: int, project: Project, db: Session = Depends(get_db)):
    existing_project = db.query(models.Projects).filter(models.Projects.id == project_id).first()
    if existing_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    existing_project.project_name = project.project_name
    db.commit()

    return 'Project updated'

@router.delete("/delete_project/{project_id}", status_code=status.HTTP_200_OK)
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Projects).filter(models.Projects.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    db.delete(project)
    db.commit()

    return 'Project deleted'
    