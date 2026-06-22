from auth import get_user
from fastapi import APIRouter, HTTPException
from models import *
import httpx
import storage


router = APIRouter()

movies_db = [{"id": 1, "title": "The Lion King", "genres": ["Adventure", "Animated", "Animals"], "year": 1994, "rating": 8.5}, 
             {"id": 2, "title": "Alien", "genres": ["Sci-fi", "Horror", "Monster", "Aliens"], "year": 1979, "rating": 8.4}, 
             {"id": 3, "title": "Spirited Away", "genres": ["Animated", "Adventure"], "year": 2001, "rating": 8.6}]

filepath = "movies.json"

storage.write_data(filepath, movies_db)

# Creates movie and puts it in storage. The template is not the same as the example database
@router.post("/create")
async def create(title, genre, year: int, rating: int):
    data = storage.read_data(filepath)
    genres = genre.split()
    new_movie = {
        "id": len(data) + 1,
        "title": title,
        "genres": genres,
        "year": year,
        "rating": rating,
    }
    data.append(new_movie)
    storage.write_data(filepath, data)

# Gets movie from storage based on id
@router.get("/read-one")
async def read_one(id_number: int):
    data = storage.read_data(filepath)
    for movie in data:
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
    data = storage.read_data(filepath)

    return data

# updates a movie detail for a movie in the list
@router.get("/update")
async def update(id_number: int, key: str, new_value):
    data = storage.read_data(filepath)
    for movie in data:
        if movie["id"] == id_number:
            if key == "year" or key == "rating":
                movie[key] = int(new_value)
            elif key == "id": # not allowed to change id number
                break
            else:
                movie[key] = new_value

    storage.write_data(filepath, data)

# removes a value from the list
@router.get("/remove")
async def update(id_number: int):
    data = storage.read_data(filepath)

    for movie in data:
        if movie["id"] == id_number:
            data.remove(movie)

    storage.write_data(filepath, data)

        


# @router.patch("/Update")
# async def update()