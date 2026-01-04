from fastapi import APIRouter
from typing import List
from app.controller.snippet_controller import get_snippets
from app.models.snippet import Snippet

router = APIRouter(prefix="/snippets", tags=["Snippets"])

@router.get("/", response_model=List[Snippet])
def list_snippets():
    return get_snippets()