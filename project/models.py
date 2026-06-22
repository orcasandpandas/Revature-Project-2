from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: int = 0
    title: str
    genres: list[str]
    year: int
    rating: float
class MovieResponse(BaseModel):
    results: list[Movie]

class Genre(BaseModel):
    id: int = 0
    name: str
class GenreResponse(BaseModel):
    genres: list[Genre]
    

