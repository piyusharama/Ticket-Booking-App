from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/shows", tags=["shows"])

@router.get("/movie/{movie_id}", response_model=list[schemas.Show])
def list_shows(movie_id: int, db: Session = Depends(get_db)):
    return crud.get_shows_by_movie(db, movie_id)

@router.get("/{show_id}/seats", response_model=list[schemas.SeatStatus])
def seats(show_id: int, db: Session = Depends(get_db)):
    seats = crud.seats_for_show(db, show_id)
    if seats is None:
        raise HTTPException(status_code=404, detail="Show not found")
    return seats

