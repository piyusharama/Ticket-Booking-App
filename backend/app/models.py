from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Table
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.dialects.postgresql import ARRAY

booking_seat_association = Table(
    'booking_seat',
    Base.metadata,
    Column('booking_id', Integer, ForeignKey('bookings.id')),
    Column('seat_id', Integer, ForeignKey('seats.id'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    bookings = relationship('Booking', back_populates='user')

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    genre = Column(String)
    description = Column(String)
    language = Column(String)
    duration = Column(Integer)
    banner = Column(String)
    shows = relationship('Show', back_populates='movie')

class Theater(Base):
    __tablename__ = 'theaters'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)
    screens = relationship('Screen', back_populates='theater')

class Screen(Base):
    __tablename__ = 'screens'
    id = Column(Integer, primary_key=True, index=True)
    theater_id = Column(Integer, ForeignKey('theaters.id'))
    screen_number = Column(Integer)
    theater = relationship('Theater', back_populates='screens')
    seats = relationship('Seat', back_populates='screen')
    shows = relationship('Show', back_populates='screen')

class Show(Base):
    __tablename__ = 'shows'
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    screen_id = Column(Integer, ForeignKey('screens.id'))
    start_time = Column(DateTime)
    price_per_seat = Column(Float)
    movie = relationship('Movie', back_populates='shows')
    screen = relationship('Screen', back_populates='shows')
    bookings = relationship('Booking', back_populates='show')

class Seat(Base):
    __tablename__ = 'seats'
    id = Column(Integer, primary_key=True, index=True)
    screen_id = Column(Integer, ForeignKey('screens.id'))
    row = Column(Integer)
    column = Column(Integer)
    screen = relationship('Screen', back_populates='seats')

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    show_id = Column(Integer, ForeignKey('shows.id'))
    payment_status = Column(String, default='pending')
    user = relationship('User', back_populates='bookings')
    show = relationship('Show', back_populates='bookings')
    seats = relationship('Seat', secondary=booking_seat_association)
