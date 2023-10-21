import tkinter as tk
import random

# Constants
GRID_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15

# Initialize the window
root = tk.Tk()
root.title("Hungry Snake")

# Initialize variables
snake = [(4, 5), (4, 4), (4, 3)]
snake_direction = (0, 1)  # (x, y) direction
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
score = 0

# Canvas setup
canvas = tk.Canvas(root, width=GRID_WIDTH * GRID_SIZE, height=GRID_HEIGHT * GRID_SIZE, bg="black")
canvas.pack()

# Draw the snake
def draw_snake():
    canvas.delete("snake")
    for segment in snake:
        x, y = segment
        canvas.create_rectangle(x * GRID_SIZE, y * GRID_SIZE, (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE, fill="green", tags="snake")

# Draw the food
def draw_food():
    x, y = food
    canvas.create_oval(x * GRID_SIZE, y * GRID_SIZE, (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE, fill="red")

# Move the snake
def move_snake():
    global snake, snake_direction, food, score

    x, y = snake[0]
    new_x = x + snake_direction[0]
    new_y = y + snake_direction[1]

    # Check for collisions
    if (new_x, new_y) in snake or new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT:
        game_over()
        return

    # Check if the snake eats the food
    if (new_x, new_y) == food:
        score += 1
        snake.insert(0, (new_x, new_y))
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        draw_food()
    else:
        snake.insert(0, (new_x, new_y))
        snake.pop()
    
    draw_snake()
    root.after(200, move_snake)

# Handle key events to change snake direction
def on_key(event):
    global snake_direction
    key = event.keysym
    if key == "Up" and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif key == "Down" and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif key == "Left" and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif key == "Right" and snake_direction != (-1, 0):
        snake_direction = (1, 0)

root.bind("<KeyPress>", on_key)

# Game over function
def game_over():
    canvas.create_text(GRID_WIDTH * GRID_SIZE // 2, GRID_HEIGHT * GRID_SIZE // 2, text=f"Game Over! Score: {score}", fill="white", font=("Arial", 20))

# Start the game
draw_snake()
draw_food()
move_snake()

root.mainloop()
