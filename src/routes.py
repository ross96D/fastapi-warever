from typing import List
from fastapi import APIRouter, Depends
from src.dependencies import get_db
from sqlalchemy.orm import Session
from src.models import Artist
from src.schemas import ArtistSchema


router = APIRouter()

@router.get("/artist")
def get_all_artist(db:Session = Depends(get_db)) -> List[ArtistSchema]:
    return Artist.get_all(db)

@router.get("/artist/{artist_id}")
def get_one_artist(artist_id: int, db:Session = Depends(get_db)) -> ArtistSchema:
    return Artist.get_one(db, artist_id)