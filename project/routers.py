from fastapi import APIRouter, HTTPException, Depends
from auth import get_user
from models import *
import httpx
import storage


router = APIRouter()

movies_db = [{"id": 1, "title": "The Lion King", "genres": ["Adventure", "Animated", "Animals"], "year": 1994, "rating": 8.5, "watched": False}, 
             {"id": 2, "title": "Alien", "genres": ["Sci-fi", "Horror", "Monster", "Aliens"], "year": 1979, "rating": 8.4, "watched": False}, 
             {"id": 3, "title": "Spirited Away", "genres": ["Animated", "Adventure"], "year": 2001, "rating": 8.6, "watched": False}]

filepath = "movies.json"

storage.write_data(filepath, movies_db)

movies_db = storage.read_data(filepath)

# Creates movie and puts it in storage. The template is not the same as the example database
@router.post("/create", response_model=Movie)
async def create(title, genre, year: int, rating: float, username: str = Depends(get_user)):
    genres = genre.split()
    new_movie = {
        "id": len(movies_db) + 1,
        "title": title,
        "genres": genres,
        "year": year,
        "rating": rating,
        "created_by": username
    }
    movies_db.append(new_movie)
    storage.write_data(filepath, movies_db)
    return new_movie

# Gets movie from storage based on id
@router.get("/read-one", response_model=Movie)
async def read_one(id_number: int, username: str = Depends(get_user)):
    for movie in movies_db:
        if movie["id"] == id_number:
            return movie
        
# Allows a movie to be searched by title and/or year
@router.get("/movie-search", response_model=MovieResponse)
def get_movie(title: str, year: Optional[int] = None, username: str = Depends(get_user)):

    if year is not None:
        return {"results" : [m for m in movies_db if m["year"] == year and title.lower() in m["title"].lower()]}
    return {"results" : [m for m in movies_db if title.lower() in m["title"].lower()]}


# Gets list from storage
@router.get("/read-all", response_model=MovieResponse,
            summary="Gets a list of all movies.  If specified, can also return a list of movies that are watch or unwatched.",
            response_description="Either a list of all movies or a list of movies that are watched/unwatched.")
async def read_all(watched: bool | None = None):
    if watched is None:
        return {"results": movies_db}
    
    filtered_movies = [m for m in movies_db if m.get("watched") == watched]

    return {"results": filtered_movies}

# Updates a movie detail for a movie in the list
@router.patch("/update", response_model=Movie)
async def update(id_number: int, key: str, new_value, username: str = Depends(get_user)):
    for movie in movies_db:
        if movie["id"] == id_number:
            if key == "year" or key == "rating":
                movie[key] = int(new_value)
            elif key == "id": # not allowed to change id number
                break
            elif key == "watched":
                movie[key] = bool(new_value)
            else:
                movie[key] = new_value
            storage.write_data(filepath, movies_db)
            return movie

# removes a value from the list
@router.delete("/remove", response_model=Movie)
async def update(id_number: int, username: str = Depends(get_user)):
    for movie in movies_db:
        if movie["id"] == id_number:
            movies_db.remove(movie)
            storage.write_data(filepath, movies_db)
            return movie
