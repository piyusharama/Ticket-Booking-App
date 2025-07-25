from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User operations

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Movie operations

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()


def get_shows_by_movie(db: Session, movie_id: int):
    return db.query(models.Show).filter(models.Show.movie_id == movie_id).all()


def seats_for_show(db: Session, show_id: int):
    show = db.query(models.Show).filter(models.Show.id == show_id).first()
    if not show:
        return []
    seats = db.query(models.Seat).filter(models.Seat.screen_id == show.screen_id).all()
    booked = (
        db.query(models.booking_seat_association.c.seat_id)
        .join(models.Booking, models.Booking.id == models.booking_seat_association.c.booking_id)
        .filter(models.Booking.show_id == show_id)
        .all()
    )
    booked_ids = {s[0] for s in booked}
    return [
        {"id": seat.id, "row": seat.row, "column": seat.column, "is_booked": seat.id in booked_ids}
        for seat in seats
    ]

# Booking operations

def create_booking(db: Session, user_id: int, show_id: int, seat_ids: list):
    # ensure requested seats are not already booked for this show
    taken = (
        db.query(models.booking_seat_association.c.seat_id)
        .join(models.Booking, models.Booking.id == models.booking_seat_association.c.booking_id)
        .filter(
            models.Booking.show_id == show_id,
            models.booking_seat_association.c.seat_id.in_(seat_ids),
        )
        .all()
    )
    if taken:
        return None

    db_booking = models.Booking(user_id=user_id, show_id=show_id, payment_status='confirmed')
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    for seat_id in seat_ids:
        seat = db.query(models.Seat).filter(models.Seat.id == seat_id).first()
        if seat:
            db_booking.seats.append(seat)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_user_bookings(db: Session, user_id: int):
    return db.query(models.Booking).filter(models.Booking.user_id == user_id).all()
