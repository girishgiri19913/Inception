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

class Track(BaseModel):
    tc: str
    name: str
    project_id:int
    
@router.get("/tracks", status_code=status.HTTP_200_OK)
async def get_tracks(db: Session = Depends(get_db)):
    tracks = db.query(models.Track).all()
    return tracks

@router.get("/tracks/{track_id}", status_code=status.HTTP_200_OK)
async def get_track(track_id: int, db: Session = Depends(get_db)):
    track = db.query(models.Track).filter(models.Track.id == track_id).first()
    if track is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")
    return track


@router.post("/create_track", status_code=status.HTTP_201_CREATED)
async def create_track(track: Track, db: Session = Depends(get_db)):
    print(track.tc)
    project_model = models.Track()  # Assuming models.Signal is the correct database model
    project_model.tc = track.tc
    project_model.name = track.name
    project_model.project_id=track.project_id

    db.add(project_model)
    db.commit()

    return "track created"


@router.put("/update_track/{track_id}", status_code=status.HTTP_200_OK)
async def update_track(track_id: int, track: Track, db: Session = Depends(get_db)):
    existing_track = db.query(models.Track).filter(models.Track.id == track_id).first()
    if existing_track is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")

    existing_track.tc = track.tc
    existing_track.name = track.name
    existing_track.project_id=track.project_id

    db.commit()
    return "Track updated"

@router.delete("/delete_track/{track_id}", status_code=status.HTTP_200_OK)
async def delete_track(track_id: int, db: Session = Depends(get_db)):
    track = db.query(models.Track).filter(models.Track.id == track_id).first()
    if track is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")

    db.delete(track)
    db.commit()
    return "Track deleted"
   

