from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow all origins for simplicity in this example
# In a production environment, restrict this to your frontend's domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

choices = ["rock", "paper", "scissors"]

# Define winning conditions: key beats value
# e.g., rock beats scissors
winning_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

@app.get("/play")
async def play_game(player_move: str):
    player_move = player_move.lower()
    if player_move not in choices:
        raise HTTPException(status_code=400, detail="Invalid player move. Choose 'rock', 'paper', or 'scissors'.")

    computer_move = random.choice(choices)

    winner = ""
    if player_move == computer_move:
        winner = "tie"
    elif winning_rules[player_move] == computer_move:
        winner = "player"
    else:
        winner = "computer"

    return {
        "player_move": player_move,
        "computer_move": computer_move,
        "winner": winner
    }

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html").read()
