from pydantic import BaseModel, Field


class ArtistSchema(BaseModel):
    artist_id: int = Field(description="id of the artist")
    name: str = Field(description="name of the artist", max_length=120)


class AlbumSchema(BaseModel):
    album_id: int = Field(description="id of the album")
    title: str = Field(description="title of the album", max_length=160)
    artist_id: int = Field(description="id of the artist that create this album")
