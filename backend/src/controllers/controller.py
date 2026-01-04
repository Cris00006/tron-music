from datetime import datetime
from typing import List
from app.model.snippet import Snippet

def get_snippet() -> List[Snippet]:
    return [
        Snippet(
            id="demo-1",
            title="First TRON Snippet",
            artist="TRON Labs",
            duration_seconds=12,
            created_at=datetime.utcnow()
        )
    ]