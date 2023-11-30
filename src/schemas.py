from pydantic import BaseModel, Field

class ArtistSchema(BaseModel):
    artist_id: int = Field(description="id of the artist")
    name: str = Field(description="name of the artist", max_length=120)