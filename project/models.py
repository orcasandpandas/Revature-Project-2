from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: int = 0
    title: str
    genres: list[str]
    year: int
    rating: float
    watched: bool = False
class MovieResponse(BaseModel):
    results: list[Movie]


    

