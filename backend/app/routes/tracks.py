from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.track import Track
from app.schemas.track import TrackCreate, TrackResponse

router = APIRouter(prefix="/tracks", tags=["Tracks"])

@router.post("/", response_model=TrackResponse)
def create_track(track: TrackCreate, db: Session = Depends(get_db)):
    db_track = Track(
        title=track.title,
        artist=track.artist,
        duration_seconds=track.duration_seconds,
        genre=track.genre
    )

    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track

@router.get("/", response_model=list[TrackResponse])
def get_tracks(db:Session = Depends(get_db)):
    return db.query(Track).all()