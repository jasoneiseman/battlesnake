"""Move logic for the Battlesnake.

Version 1: pick any move that doesn't run into a wall, our own body,
or another snake's body.
"""

import random

DIRECTIONS = {
    "up": (0, 1),
    "down": (0, -1),
    "left": (-1, 0),
    "right": (1, 0),
}


def choose_move(game_state: dict) -> str:
    board = game_state["board"]
    you = game_state["you"]
    head = you["head"]
    width, height = board["width"], board["height"]

    # Every body segment on the board is an obstacle. A snake's tail moves
    # out of the way next turn unless it just ate (stacked tail), but for
    # v1 we stay conservative and treat all segments as blocked.
    occupied = set()
    for snake in board["snakes"]:
        for segment in snake["body"]:
            occupied.add((segment["x"], segment["y"]))

    safe_moves = []
    for move, (dx, dy) in DIRECTIONS.items():
        x, y = head["x"] + dx, head["y"] + dy
        if not (0 <= x < width and 0 <= y < height):
            continue
        if (x, y) in occupied:
            continue
        safe_moves.append(move)

    if not safe_moves:
        # No safe option; any move loses, so just pick one.
        return "down"

    return random.choice(safe_moves)
