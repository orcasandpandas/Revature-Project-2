from fastapi import APIRouter, HTTPException
from models import *
import httpx


router = APIRouter()

TMDB_API_KEY = "034f84e71360ce56922495f811ae84d6"
TMDB_BASE_URL = "https://api.themoviedb.org/3"


# Gets details of a movie
@router.get("/movies", response_model=MovieResponse)
async def get_movie(kw, year):
    url = f"{TMDB_BASE_URL}/discover/movie"

    params = {"api_key": TMDB_API_KEY, 
              "with_keywords": kw,
              "year": year}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code, 
                detail="Error fetching data from TMDB. Check the movie ID or API key."
            )
    
    data = response.json()

    return data

# Gets Genres
@router.get("/genres", response_model=GenreResponse)
async def get_genres():
    url = f"{TMDB_BASE_URL}/discover/movie"