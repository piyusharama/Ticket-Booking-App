from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.post("/", response_model=schemas.Booking)
def book_seats(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    db_booking = crud.create_booking(db, booking.user_id, booking.show_id, booking.seat_ids)
    if db_booking is None:
        raise HTTPException(status_code=400, detail="Selected seats already booked")
    return db_booking

@router.get("/user/{user_id}", response_model=list[schemas.Booking])
def user_bookings(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_bookings(db, user_id)
