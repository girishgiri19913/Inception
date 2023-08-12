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

class Route(BaseModel):
    prefix : str
    category:str
    s_signal:str
    x_signal:str
    g_button:str
    route:str
    u_route:str
    number_input_yu:int
    option_input_yu:str
    number_input_y:int
    option_input_y:str
    number_input_yy:int
    option_input_yy:str
    number_input_g:int
    option_input_g:str
    project_id: int  # Foreign key for the project
    
@router.get("/routes", status_code=status.HTTP_200_OK)
async def get_routes(db: Session = Depends(get_db)):
    routes = db.query(models.Route).all()
    return routes

@router.get("/routes/{route_id}", status_code=status.HTTP_200_OK)
async def get_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(models.Route).filter(models.Route.id == route_id).first()
    if route is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")
    return route

@router.post("/create_route", status_code=status.HTTP_201_CREATED)
async def create_route(route: Route, db: Session = Depends(get_db)):
    print(route.category)
    project_model = models.Route()
    project_model.prefix =route.prefix
    project_model.category = route.category  # Assuming models.Signal is the correct database model
    project_model.s_signal = route.s_signal
    project_model.x_signal = route.x_signal
    project_model.g_button = route.g_button
    project_model.route = route.route
    project_model.u_route = route.u_route
    project_model.number_input_yu = route.number_input_yu
    project_model.option_input_yu = route.option_input_yu
    project_model.number_input_y= route.number_input_y
    project_model.option_input_y = route.option_input_y
    project_model.number_input_yy = route.number_input_yy
    project_model.option_input_yy = route.option_input_yy
    project_model.number_input_g = route.number_input_g
    project_model.option_input_g = route.option_input_g
    project_model.project_id = route.project_id  # Set the project_id foreign key


    db.add(project_model)
    db.commit()

    return "Route created"

@router.put("/update_route/{route_id}", status_code=status.HTTP_200_OK)
async def update_route(route_id: int, route: Route, db: Session = Depends(get_db)):
    existing_route = db.query(models.Route).filter(models.Route.id == route_id).first()
    if existing_route is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")

    existing_route.prefix = route.prefix
    existing_route.category = route.category
    existing_route.s_signal = route.s_signal
    existing_route.x_signal = route.x_signal
    existing_route.g_button = route.g_button
    existing_route.route = route.route
    existing_route.u_route = route.u_route
    existing_route.number_input_yu = route.number_input_yu
    existing_route.option_input_yu = route.option_input_yu
    existing_route.number_input_y = route.number_input_y
    existing_route.option_input_y = route.option_input_y
    existing_route.number_input_yy = route.number_input_yy
    existing_route.option_input_yy = route.option_input_yy
    existing_route.number_input_g = route.number_input_g
    existing_route.option_input_g = route.option_input_g
    existing_route.project_id = route.project_id  # Update the project_id foreign key


    db.commit()
    return "Route updated"

@router.delete("/delete_route/{route_id}", status_code=status.HTTP_200_OK)
async def delete_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(models.Route).filter(models.Route.id == route_id).first()
    if route is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")

    db.delete(route)
    db.commit()
    return "Route deleted"