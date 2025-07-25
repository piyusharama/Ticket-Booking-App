from fastapi import FastAPI
from .database import Base, engine
from .routers import auth, movies, bookings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ticket Booking API")

app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(bookings.router)

@app.get("/")
def root():
    return {"message": "API running"}
