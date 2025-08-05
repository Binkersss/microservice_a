from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
import json

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Load data from JSON file on startup
with open("games.json", "r", encoding="utf-8") as f:
    games_db = json.load(f)

@app.get("/games")
def get_games(
    name: Optional[str] = Query(None, description="Filter by game name substring"),
    releaseYear: Optional[int] = Query(None, description="Filter by release year"),
    genre: Optional[str] = Query(None, description="Filter by genre (case insensitive)")
):
    results = games_db

    # Filter by name substring (case insensitive)
    if name:
        results = [g for g in results if name.lower() in g["name"].lower()]

    # Filter by release year exact match
    if releaseYear:
        results = [g for g in results if g["releaseYear"] == releaseYear]

    # Filter by genre (case insensitive exact match)
    if genre:
        results = [g for g in results if g["genre"].lower() == genre.lower()]

    return results

