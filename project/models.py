from pydantic import BaseModel
from typing import Optional

class MovieResponse(BaseModel):
    id: int
    title: str
    release_date: str
