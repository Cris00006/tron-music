from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings import settings
from app.routes.ping import router as ping_router
from app.routes.tracks import router as tracks_router
from app.database import Base, engine

app = FastAPI(title=settings.APP_NAME)

# CORS (para Flutter / Web)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(ping_router)
app.include_router(tracks_router)

# Root
@app.get("/")
def root():
    return {"status": "TRON backend online"}

# Create tables (MVP only)
Base.metadata.create_all(bind=engine)
