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
@router.post("/create")
async def create(genre, title, year, rating):
    data = storage.read_data("movies.json")
    new_movie = {
        "id": len(data) + 1,
        "title": title,
        "genres": genre,
        "year": year,
        "rating": rating,
    }
    data.append(new_movie)
    storage.write_data("movies.json", data)

# Gets movie from storage based on id
@router.get("/read-one")
async def read_one(id_number: int):
    data = storage.read_data("movies.json")
    for movie in data:
        print(type(movie))
        if movie["id"] == id_number:
            return movie
        
# Allows a movie to be searched by title and/or year
@router.get("/movie-search", response_model=MovieResponse)
def get_movie(title: str, year: Optional[int] = None):

    if year is not None:
        return {"results" : [m for m in movies_db if m["year"] == year and title.lower() in m["title"].lower()]}
    return {"results" : [m for m in movies_db if title.lower() in m["title"].lower()]}


# Gets list from storage
@router.get("/read-all")
async def read_all():
    data = storage.read_data("movies.json")

    return data



# @router.patch("/Update")
# async def update()