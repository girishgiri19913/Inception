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

class Signal(BaseModel):
    point: int
    a_point: str
    a_Track_point: str
    b_point: str
    b_Track_point: str
    char: str
    project_id:int

@router.get("/signals", status_code=status.HTTP_200_OK)
async def get_signals(db: Session = Depends(get_db)):
    signals = db.query(models.Signal).all()
    return signals

@router.get("/signals/{signal_id}", status_code=status.HTTP_200_OK)
async def get_signal(signal_id: int, db: Session = Depends(get_db)):
    signal = db.query(models.Signal).filter(models.Signal.id == signal_id).first()
    if signal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Signal not found")
    return signal


@router.post("/create_signal", status_code=status.HTTP_201_CREATED)
async def create_signal(signal: Signal, db: Session = Depends(get_db)):
    print(signal.point)
    project_model = models.Signal()  # Assuming models.Signal is the correct database model
    project_model.point = signal.point
    project_model.a_point = signal.a_point
    project_model.a_Track_point = signal.a_Track_point
    project_model.b_point = signal.b_point
    project_model.b_Track_point = signal.b_Track_point
    project_model.char = signal.char
    project_model.project_id=signal.project_id

    db.add(project_model)
    db.commit()



    return "Signal created"

@router.put("/update_signal/{signal_id}", status_code=status.HTTP_200_OK)
async def update_signal(signal_id: int, signal: Signal, db: Session = Depends(get_db)):
    existing_signal = db.query(models.Signal).filter(models.Signal.id == signal_id).first()
    if existing_signal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Signal not found")

    existing_signal.point = signal.point
    existing_signal.a_point = signal.a_point
    existing_signal.a_Track_point = signal.a_Track_point
    existing_signal.b_point = signal.b_point
    existing_signal.b_Track_point = signal.b_Track_point
    existing_signal.char = signal.char
    existing_signal.project_id=signal.project_id

    db.commit()
    return "Signal updated"

@router.delete("/delete_signal/{signal_id}", status_code=status.HTTP_200_OK)
async def delete_signal(signal_id: int, db: Session = Depends(get_db)):
    signal = db.query(models.Signal).filter(models.Signal.id == signal_id).first()
    if signal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Signal not found")

    db.delete(signal)
    db.commit()
    return "Signal deleted"

