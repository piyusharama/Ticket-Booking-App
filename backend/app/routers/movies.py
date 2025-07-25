from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/", response_model=list[schemas.Movie])
def list_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip=skip, limit=limit)
