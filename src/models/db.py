from abc import ABC, abstractclassmethod
from src.models.base import (
    Album,
    Artist,
    Track,
    MediaType,
    Genre,
)
from src.schemas import (
    ArtistSchema,
    AlbumSchema,
    TrackSchema,
    GenreSchema,
    MediaTypeSchema,
)
from sqlalchemy import text, ColumnElement
from sqlalchemy.orm import Session
from typing import Generic, TypeVar


M = TypeVar("M")
S = TypeVar("S")


class _Crud(Generic[M, S], ABC):
    model_class: M

    @abstractclassmethod
    def one_filter(self, id: int) -> ColumnElement[bool]:
        pass

    def get_all(self, db: Session) -> list[M]:
        return [x.parse() for x in db.query(self.model_class).all()]

    def _get_one(self, db: Session, id: int) -> S:
        return db.query(self.model_class).filter(self.one_filter(id)).one().parse()

    def get_one(self, db: Session, id: int):
        return self._get_one(db, id)


class _ArtistCrud(_Crud[Artist, ArtistSchema]):
    def __init__(self) -> None:
        self.model_class = Artist
        super().__init__()

    def one_filter(self, id: int):
        return Artist.ArtistId == id

    def get_albums(self, db: Session, artist_id: int) -> list[AlbumSchema]:
        return [x.parse() for x in db.query(Album).filter_by(ArtistId=artist_id).all()]

    def get_tracks(self, db: Session, artist_id: int) -> list[TrackSchema]:
        query = db.execute(
            text(
                """
                SELECT "Track".* FROM "Track" 
                    LEFT JOIN "Album" ON "Track"."AlbumId" = "Album"."AlbumId"
                    LEFT JOIN "Artist" ON "Album"."ArtistId" = "Artist"."ArtistId"
                WHERE "Artist"."ArtistId"=:artist_id
            """
            ).bindparams(artist_id=artist_id),
        )
        result: list[TrackSchema] = []
        for row in query:
            result.append(
                TrackSchema(
                    track_id=row.TrackId,
                    album_id=row.AlbumId,
                    genre_id=row.GenreId,
                    media_type_id=row.MediaTypeId,
                    bytes=row.Bytes,
                    composer=row.Composer,
                    milliseconds=row.Milliseconds,
                    name=row.Name,
                    unit_price=row.UnitPrice,
                )
            )

        return result


class _AlbumCrud(_Crud[Album, AlbumSchema]):
    def __init__(self) -> None:
        self.model_class = Album
        super().__init__()

    def one_filter(self, id: int):
        return Album.AlbumId == id


class _TrackCrud(_Crud[Track, TrackSchema]):
    def __init__(self) -> None:
        self.model_class = Track
        super().__init__()

    def one_filter(self, id: int) -> ColumnElement[bool]:
        return Track.TrackId == id

    def get_all_by_album(self, db: Session, album_id: int) -> list[TrackSchema]:
        result = [x.parse() for x in db.query(Track).filter(Track.AlbumId == album_id).all()]
        print(result[0])
        return result


class _MediaTypeCrud(_Crud[MediaType, MediaTypeSchema]):
    def __init__(self) -> None:
        self.model_class = MediaType
        super().__init__()

    def one_filter(id: int) -> ColumnElement[bool]:
        return MediaType.MediaTypeId == id


class _GenreCrud(_Crud[Genre, GenreSchema]):
    def __init__(self) -> None:
        self.model_class = Genre
        super().__init__()

    def one_filter(id: int) -> ColumnElement[bool]:
        return Genre.GenreId == id


class _Models:
    def __init__(self) -> None:
        self.album = _AlbumCrud()
        self.artist = _ArtistCrud()
        self.track = _TrackCrud()
        self.genre = _GenreCrud()
        self.mediaType = _MediaTypeCrud()


models = _Models()
