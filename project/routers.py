from fastapi import APIRouter, HTTPException, Depends, Query
from auth import get_user
from models import *
import storage


router = APIRouter()

filepath = "movies.json"


movies_db = storage.read_data(filepath)

# Creates movie and puts it in storage. 
@router.post("/create", response_model=Movie,
    tags=["Movies", "Create"],
    summary="Create a new movie entry",
    description="Adds a new movie to the database. The genre string will be split into a list of individual genres.",)
async def create(title: str = Query(..., description="The full title of the movie."),
                 genre: str = Query(..., description="The genres of the movie, each separated by a space"), 
                 year: int = Query(..., description="The 4-digit release year (e.g., 2026)"), 
                 rating: float = Query(..., descrption="The rating of the movie on a scale from 1 to 10."), 
                 username: str = Depends(get_user)):
    genres = genre.split()
    new_movie = {
        "id": len(movies_db) + 1,
        "title": title,
        "genres": genres (description="Input is a string with genres separated by a space"),
        "year": year,
        "rating": rating,
        "created_by": username
    }
    movies_db.append(new_movie)
    storage.write_data(filepath, movies_db)
    return new_movie

# Gets movie from storage based on id
@router.get("/read-one", response_model=Movie,
    tags=["Movies", "Read"],
    summary="Reads a movie by id",
    description="Reads an individual movie directy though its id.")

async def read_one(id_number: int = Query(..., description="The database id of the movie."), username: str = Depends(get_user)):
    for movie in movies_db:
        if movie["id"] == id_number:
            return movie
        
# Allows a movie to be searched by title and/or year
@router.get("/movie-search", response_model=MovieResponse,
    tags=["Movies", "Read"],
    summary="Allows a movie to be searched by title",
    description="Queries for any  movies matching the inputted keywords; year is optional.")
def get_movie(title: str = Query(..., description="The partial or full title of the movie to search for.  Not case-sensitive")
              , year: Optional[int] = Query(None, description="The 4-digit release year (e.g., 2026), optional."), username: str = Depends(get_user)):

    if year is not None:
        return {"results" : [m for m in movies_db if m["year"] == year and title.lower() in m["title"].lower()]}
    return {"results" : [m for m in movies_db if title.lower() in m["title"].lower()]}


# Gets list from storage
@router.get("/read-all", response_model=MovieResponse,
    tags=["Movies", "Read"],
    summary="Gets a list of all movies.  If specified, can also return a list of movies that are watch or unwatched.",
    response_description="Either a list of all movies or a list of movies that are watched/unwatched.")
async def read_all(watched: Optional[int] = Query(None, description="An optional parameter to get only watched movies (True) or unwatched (False).")):
    if watched is None:
        return {"results": movies_db}
    
    filtered_movies = [m for m in movies_db if m.get("watched") == watched]

    return {"results": filtered_movies}

# Updates a movie detail for a movie in the list
@router.patch("/update", response_model=Movie,
    tags=["Movies", "Update"],
    summary="Updates a specific movie's detail",
    description="Allows the following details of a movie to be updated: year, rating, and watched.")
async def update(id_number: int = Query(..., description="The database id of the movie"), 
                 key: str = Query(..., description="The name of the parameter to be changed; can be year, rating, or watched"), 
                 new_value = Query(..., description="The new value; must be int for year, float for rating and boolean for watched"), username: str = Depends(get_user)):
    for movie in movies_db:
        if movie["id"] == id_number:
            if key == "year":
                movie[key] = int(new_value)
            elif key == "rating":
                movie[key] = float(new_value)
            elif key == "id": # not allowed to change id number
                break
            elif key == "watched":
                movie[key] = bool(new_value)
            else:
                movie[key] = new_value
            storage.write_data(filepath, movies_db)
            return movie

# removes a value from the list
@router.delete("/remove", response_model=Movie,
    tags=["Movies", "Delete"],
    summary="Removes a movie from the database",
    description="Allows a movie to be removed by id.")
async def update(id_number: int = Query(..., description="The database id of the movie to be removed."), username: str = Depends(get_user)):
    for movie in movies_db:
        if movie["id"] == id_number:
            movies_db.remove(movie)
            storage.write_data(filepath, movies_db)
            return movie
