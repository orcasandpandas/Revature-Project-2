from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    genre_ids: list[int] 
    id: int = 0
    title: str
    overview: str
    release_date: str
class MovieResponse(BaseModel):
    page: int = 0
    results: list[Movie]
class MovieResponse(BaseModel):
    id: int
    title: str
    release_date: str

class Genre(BaseModel):
    id: int = 0
    name: str
class GenreResponse(BaseModel):
    genres: list[Genre]
    

