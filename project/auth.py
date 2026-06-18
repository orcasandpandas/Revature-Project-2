import httpx
import secrets
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

security = HTTPBasic()

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMzRmODRlNzEzNjBjZTU2OTIyNDk1ZjgxMWFlODRkNiIsIm5iZiI6MTc4MTgxNTY2MC4xNDgsInN1YiI6IjZhMzQ1OTZjYTQ5NzZiYjYyOGQwYWFmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Gr9QI7VAy2F8PN5gXZE8aiEjrVWg8jh5C_jfhXQYzpw"
}


