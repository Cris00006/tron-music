from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TrackCreate(BaseModel):
    title: str
    artist: str
    duration_seconds: int
    genre: Optional[str] = None

class TrackResponse(TrackCreate):
    id: int
    created_at:datetime

class Config:
    from_atributes = True