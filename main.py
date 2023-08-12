from fastapi import FastAPI
import models
from database import engine
from routers import create_signal,create_project,create_route,create_track
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(create_project.router)
app.include_router(create_signal.router)
app.include_router(create_route.router)
app.include_router(create_track.router)


origins = [
    "http://localhost",
    "http://localhost:9006",  # Add any other frontend URLs you want to allow
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
