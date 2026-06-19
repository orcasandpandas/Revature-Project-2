from fastapi import APIRouter, HTTPException
from models import *


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


genres = {1 : "Animated", 2 : "Horror"}


# Gets movies matching a query
@router.get("/movies", response_model=MovieResponse)
def get_movie(title: str, year: Optional[int] = None):

    if year is not None:
        return {"results" : [m for m in movies_db if m["year"] == year and title.lower() in m["title"].lower()]}
    return {"results" : [m for m in movies_db if title.lower() in m["title"].lower()]}

    

    raise HTTPException(status_code=404, detail=f"Movie with title {title} from year {year} not found")


# # Gets Genres
# @router.get("/genres", response_model=GenreResponse)
# async def get_genres():

#     params = {}

#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, params=params)

#     if response.status_code != 200:
#             raise HTTPException(
#                 status_code=response.status_code, 
#                 detail="Error fetching data from TMDB. Check the movie ID or API key."
#             )
    
#     data = response.json()
    
#     return data