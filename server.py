import logging
import os

from flask import Flask, jsonify, request

from logic import choose_move

app = Flask(__name__)
logging.getLogger("werkzeug").setLevel(logging.WARNING)


@app.get("/")
def info():
    # Appearance and metadata: https://docs.battlesnake.com/api/requests/info
    return jsonify(
        {
            "apiversion": "1",
            "author": "",
            "color": "#2E8B57",
            "head": "default",
            "tail": "default",
            "version": "0.1.0",
        }
    )


@app.post("/start")
def start():
    game = request.get_json()
    print(f"GAME START: {game['game']['id']}")
    return "ok"


@app.post("/move")
def move():
    game = request.get_json()
    next_move = choose_move(game)
    print(f"TURN {game['turn']}: {next_move}")
    return jsonify({"move": next_move})


@app.post("/end")
def end():
    game = request.get_json()
    print(f"GAME OVER: {game['game']['id']}")
    return "ok"


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    print(f"Running Battlesnake at http://{host}:{port}")
    app.run(host=host, port=port)
