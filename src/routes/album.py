from typing import List
from fastapi import APIRouter, Depends
from src.dependencies import get_db
from sqlalchemy.orm import Session
from src.models.db import models
from src.schemas import AlbumSchema, TrackSchema


router = APIRouter(prefix="/albums", tags=["Albums"])


@router.get("/")
def all_artists(db: Session = Depends(get_db)) -> List[AlbumSchema]:
    return models.album.get_all(db)


@router.get("/{album_id}")
def get_artist(album_id: int, db: Session = Depends(get_db)) -> List[AlbumSchema]:
    return models.album.get_one(db, album_id)


@router.get("/{album_id}/tracks")
def get_tracks(album_id: int, db: Session = Depends(get_db)) -> List[TrackSchema]:
    return models.track.get_all_by_album(db, album_id)
