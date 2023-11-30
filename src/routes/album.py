from typing import List
from fastapi import APIRouter, Depends
from src.dependencies import get_db
from sqlalchemy.orm import Session
from src.models import Album, Track
from src.schemas import AlbumSchema


router = APIRouter(prefix="/albums", tags=["Albums"])


@router.get("/")
def all_artists(db: Session = Depends(get_db)) -> List[AlbumSchema]:
    return Album.get_all(db)


@router.get("/{album_id}")
def get_artist(album_id: int, db: Session = Depends(get_db)) -> List[AlbumSchema]:
    return Album.get_one(db, album_id)


@router.get("/{album_id}/tracks")
def get_tracks(album_id: int, db: Session = Depends(get_db)) -> List[AlbumSchema]:
    return Track.get_all_by_album(db, album_id)
