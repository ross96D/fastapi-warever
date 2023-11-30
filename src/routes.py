from typing import List
from fastapi import APIRouter, Depends
from src.dependencies import get_db
from sqlalchemy.orm import Session
from src.models import Artist
from src.schemas import ArtistSchema


router = APIRouter(prefix="/artist")


@router.get("/")
def all_artist(db: Session = Depends(get_db)) -> List[ArtistSchema]:
    return Artist.get_all(db)


@router.get("/{artist_id}")
def artist(artist_id: int, db: Session = Depends(get_db)) -> ArtistSchema:
    return Artist.get_one(db, artist_id)


@router.get("/{artist_id}/albums")
def albums(artist_id: int, db: Session = Depends(get_db)):
    return Artist.get_albums(db=db, artist_id=artist_id)
