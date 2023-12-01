from typing import List
from fastapi import APIRouter, Depends
from src.dependencies import get_db
from sqlalchemy.orm import Session
from src.models.db import models
from src.schemas import ArtistSchema, AlbumSchema, TrackSchema


router = APIRouter(prefix="/artists", tags=["Artists"])


@router.get("/")
def all_artist(db: Session = Depends(get_db)) -> List[ArtistSchema]:
    return models.artist.get_all(db)


@router.get("/{artist_id}")
def artist(artist_id: int, db: Session = Depends(get_db)) -> ArtistSchema:
    return models.artist.get_one(db, artist_id)


@router.get("/{artist_id}/albums")
def albums(artist_id: int, db: Session = Depends(get_db)) -> list[AlbumSchema]:
    return models.artist.get_albums(db=db, artist_id=artist_id)


@router.get("/{artist_id}/tracks")
def tracks(artist_id: int, db: Session = Depends(get_db)) -> list[TrackSchema]:
    return models.artist.get_tracks(db, artist_id)
