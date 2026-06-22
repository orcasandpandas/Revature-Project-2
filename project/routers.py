from fastapi import APIRouter, HTTPException
from models import *
import httpx
import storage


router = APIRouter()

movies_db = [{
        "id": 1,
        "title": "The Lion King",
        "genres": ["Adventure", "Animated", "Animals"],
        "year": 1994,
        "rating": 8.5
    },
    {
        "id": 2,
        "title": "Alien",
        "genres": ["Sci-fi", "Horror", "Monster", "Aliens"],
        "year": 1979,
        "rating": 8.4
    },
    {
        "id": 3,
        "title": "Spirited Away",
        "genres": ["Animated", "Adventure"],
        "year": 2001,
        "rating": 8.6
    }
]

storage.write_data("movies.json", movies_db)

# Creates movie and puts it in storage. The template is not the same as the example database
@router.post("/Create")
async def create(genre, title, release_date):
    data = storage.read_data("movies.json")
    new_movie = {
        "id": len(data) + 1,
        "genre": genre,
        "title": title,
        "release date": release_date
    }
    data.append(new_movie)
    storage.write_data("movies.json", data)

# Gets movie from storage based on id
@router.get("/ReadOne")
async def read_one(id_number: int):
    data = storage.read_data("movies.json")
    for movie in data:
        print(type(movie))
        if movie["id"] == id_number:
            return movie

# Gets list from storage
@router.get("/ReadAll")
async def read_all():
    data = storage.read_data("movies.json")

    return data

# @router.patch("/Update")
# async def update()