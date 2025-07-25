from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Movie(BaseModel):
    id: int
    name: str
    genre: Optional[str]
    description: Optional[str]
    language: Optional[str]
    duration: Optional[int]
    banner: Optional[str]

    class Config:
        orm_mode = True

class Theater(BaseModel):
    id: int
    name: str
    location: Optional[str]

    class Config:
        orm_mode = True

class Screen(BaseModel):
    id: int
    theater_id: int
    screen_number: int

    class Config:
        orm_mode = True

class Show(BaseModel):
    id: int
    movie_id: int
    screen_id: int
    start_time: datetime
    price_per_seat: float

    class Config:
        orm_mode = True

class Seat(BaseModel):
    id: int
    screen_id: int
    row: int
    column: int

    class Config:
        orm_mode = True

class Booking(BaseModel):
    id: int
    user_id: int
    show_id: int
    payment_status: str
    seat_ids: List[int]

    class Config:
        orm_mode = True


class BookingCreate(BaseModel):
    user_id: int
    show_id: int
    seat_ids: List[int]


class SeatStatus(BaseModel):
    id: int
    row: int
    column: int
    is_booked: bool
