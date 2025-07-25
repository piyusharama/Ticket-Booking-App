# Ticket Booking App

This repository contains a minimal skeleton for a BookMyShow-like ticket booking platform.

## Stack
- **Backend**: FastAPI (Python)
- **Frontend**: React using Next.js
- **Database**: PostgreSQL

## Structure
- `backend/` – FastAPI application
- `frontend/` – Next.js app (placeholders)
- `docker-compose.yml` – Development setup

Run `docker-compose up` to start the application.

### API Overview

- `POST /auth/signup` – register new user
- `POST /auth/login` – obtain JWT token
- `GET /movies/` – list movies
- `GET /shows/movie/{movie_id}` – list shows for a movie
- `GET /shows/{show_id}/seats` – seat availability for a show
- `POST /bookings/` – book seats
