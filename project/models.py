from pydantic import BaseModel
from typing import Optional

class MovieResponse(BaseModel):
    id: int
    name: str
    department: str
    salary: int
