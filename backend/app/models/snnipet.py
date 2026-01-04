from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Snippet(BaseModel)
    id: str
    title: str
    artist: str
    duration_seconds: int
    created_at: datetime
    