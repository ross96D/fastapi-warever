from typing import Optional
from pydantic import BaseModel, Field


class ArtistSchema(BaseModel):
    artist_id: int = Field(description="id of the artist")
    name: Optional[str] = Field(description="name of the artist", max_length=120)


class AlbumSchema(BaseModel):
    album_id: int = Field(description="id of the album")
    title: str = Field(description="title of the album", max_length=160)
    artist_id: int = Field(description="id of the artist that create this album")


class TrackSchema(BaseModel):
    track_id: int = Field(description="id of the track")
    name: str = Field(description="name of the track")
    album_id: int = Field(description="id of the album corresponding to the track")
    media_type_id: int = Field(description="id of the media type corresponding to the track")
    genre_id: Optional[int] = Field(description="id of the genre corresponding to the track")
    composer: Optional[str] = Field(description="composer?")
    milliseconds: int = Field(description="time of the track in milliseconds")
    bytes: Optional[int] = Field(description="bytes of the track")
    unit_price: float = Field(description="price")


class GenreSchema(BaseModel):
    genre_id: int = Field(description="id of the genre")
    name: Optional[str] = Field(max_length=120, description="name of the genre")


class MediaTypeSchema(BaseModel):
    media_type_id: int = Field(description="id of the media_type")
    name: Optional[str] = Field(max_length=120, description="name of the media type")
