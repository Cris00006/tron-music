from fastapi import APIRouter

router = APIRouter(prefix="/ping",tags=["Health"])

@router.get("")
def ping():
    return {"status": "ok"}
