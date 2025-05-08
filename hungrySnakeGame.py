#!/usr/bin/env python

"""
-----------------------------------------------
Snake Game using Python Turtle

This game is a simple version of the classic Snake game.
It was created for Cambourne Young Techies - Tech Club students to learn about:
- Basic Python programming
- Turtle graphics
- Handling keyboard events
- Game loops and logic

How it works:
- The snake moves around the screen, growing when it eats food.
- The player controls the snake using the arrow keys.
- The game resets if the snake crashes into itself.
- The snake wraps around if it goes off the screen.

Controls:
- Up arrow:    Move up
- Down arrow:  Move down
- Left arrow:  Move left
- Right arrow: Move right

Install:
Install turtle and random modules, if you don’t have it already installed, open your cmd and type in the following command.
>pip install turtle
>pip install random2

Author: AHS
Date: 08-05-2025
-----------------------------------------------
"""

import turtle
import random

# --- Game Settings ---
SCREEN_WIDTH: int = 500           # Width of the game window
SCREEN_HEIGHT: int = 500          # Height of the game window
FOOD_SIZE: int = 10               # Size of the food square
MOVE_DELAY: int = 100             # Delay between moves in milliseconds

# Movement offsets for each direction (x, y)
OFFSETS: dict = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# --- Functions ---

def reset_game() -> None:
    """Resets the game:
    - Initializes the snake's position and direction
    - Places food at a random location
    - Starts the snake moving
    """
    global snake, snake_direction, food_position

    # The snake starts with 5 segments, vertically aligned
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]        # list
    snake_direction = "up"                                      # str

    # Place the food at a random position
    food_position = get_random_food_position()                  # tuple
    food.goto(food_position)

    # Start moving the snake
    move_snake()

def move_snake() -> None:
    """Moves the snake one step forward:
    - Adds a new head in the current direction
    - Checks for collisions with itself
    - Checks for food collision
    - Wraps around screen if necessary
    """
    global snake_direction

    # Copy the current head and calculate the new head position
    new_head: list = snake[-1].copy()
    new_head[0] += OFFSETS[snake_direction][0]
    new_head[1] += OFFSETS[snake_direction][1]

    # If the snake bites itself, reset the game
    if new_head in snake[:-1]:
        reset_game()
        return

    # Add new head to the snake body
    snake.append(new_head)

    # If no food collision, remove the tail (snake moves forward)
    if not check_food_collision():
        snake.pop(0)

    # Wrap the snake around if it goes off-screen
    wrap_around_screen(new_head)

    # Clear the previous snake and redraw it
    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    # Update the screen and schedule the next move
    screen.update()
    turtle.ontimer(move_snake, MOVE_DELAY)

def check_food_collision() -> bool:
    """Checks if the snake's head is touching the food.
    Returns True if food is eaten, False otherwise.
    """
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        # Move the food to a new random position
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position() -> tuple:
    """Returns a random (x, y) position within screen bounds."""
    x: int = random.randint(-SCREEN_WIDTH // 2 + FOOD_SIZE, SCREEN_WIDTH // 2 - FOOD_SIZE)
    y: int = random.randint(-SCREEN_HEIGHT // 2 + FOOD_SIZE, SCREEN_HEIGHT // 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1: list, pos2: tuple) -> float:
    """Calculates the distance between two positions (x, y)."""
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def wrap_around_screen(position: list) -> None:
    """If the snake goes off the screen, wraps it around to the other side."""
    if position[0] > SCREEN_WIDTH / 2:
        position[0] -= SCREEN_WIDTH
    elif position[0] < -SCREEN_WIDTH / 2:
        position[0] += SCREEN_WIDTH
    if position[1] > SCREEN_HEIGHT / 2:
        position[1] -= SCREEN_HEIGHT
    elif position[1] < -SCREEN_HEIGHT / 2:
        position[1] += SCREEN_HEIGHT

# --- Direction Controls ---

def go_up() -> None:
    """Change snake's direction to up (if not going down)."""
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down() -> None:
    """Change snake's direction to down (if not going up)."""
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left() -> None:
    """Change snake's direction to left (if not going right)."""
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def go_right() -> None:
    """Change snake's direction to right (if not going left)."""
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

# --- Main Program ---

if __name__ == "__main__":
    # Set up the game window
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Snake Game")
    screen.bgcolor("blue")
    screen.tracer(0)  # Turn off auto-updating for smoother animation

    # Create the snake pen (the square used to draw the snake)
    pen = turtle.Turtle("square")
    pen.penup()

    # Create the food turtle
    food = turtle.Turtle()
    food.shape("square")
    food.color("yellow")
    food.shapesize(FOOD_SIZE / 20)  # Scale the food size
    food.penup()

    # Set up keyboard controls
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")

    # Start the game
    reset_game()

    # Keep the window open
    turtle.done()
