import secrets
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

router = APIRouter()

security = HTTPBasic()

USERS = {
    "admin": "password123",
    "user1": "mypassword"
}

def get_user(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    stored_password = USERS[credentials.username, ""]
    password_correct = secrets.compare_digest(
        credentials.password.encode('utf-8'), 
        stored_password.encode('utf-8')
    )
    if not password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@router.get("/movies/me", tags=["Auth"])
def get_profile(username: str = Depends(get_user)):
    return {
        "username": username,
        "message": f"Hello {username}, you are authenticated."
    }

@router.get("/movies", tags=["Auth"])
def get_profile(username: str = Depends(get_user)):
    return {"Users": [], "requested_by": username}