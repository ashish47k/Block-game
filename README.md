# Block Game - Pygame Project (2023)

This is a Pygame-based "Block Game" project I developed in 2023 as part of my exploration of Python game development. The game allows players to control a player block while avoiding falling obstacles, with additional features like difficulty levels, score tracking, and a restart functionality.

## Game Overview

In this game, the player controls a blue block that can move left and right along the bottom of the screen. Red obstacles fall from the top, and the goal is to avoid these obstacles for as long as possible. The player can choose between different difficulty levels (Easy, Medium, Hard), each with increasing speed for the obstacles. The game also includes a lives system, score tracking, and a high score feature.

## Features

- **Difficulty Levels**: Choose between Easy, Medium, and Hard. Higher difficulty levels increase the speed of the falling obstacles.
- **Multiple Obstacles**: Obstacles fall from random positions and at varying speeds.
- **Lives System**: The player has 3 lives; a life is lost each time an obstacle is hit.
- **Score and High Score Tracking**: The player earns points for each obstacle avoided, and the highest score is saved for the session.
- **Restart Functionality**: After the game ends, players can restart with the same difficulty level without returning to the main menu.
- **User Interface**: Start, Quit, and Restart buttons to navigate the game.

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/BlockGame.git
    cd BlockGame
    ```

2. **Install Dependencies**:
   - The game requires Pygame. Install it via pip if you haven’t already:
    ```bash
    pip install pygame
    ```

3. **Run the Game**:
    ```bash
    python main.py
    ```

## How to Play

1. **Start the Game**: Launch the game, choose a difficulty level (Easy, Medium, or Hard), and start moving your block.
2. **Move the Block**: Use the **Left** and **Right** arrow keys to control the blue block at the bottom.
3. **Avoid Obstacles**: Try to avoid the red obstacles that fall from the top of the screen.
4. **Track Your Lives**: The player starts with 3 lives. Each collision with an obstacle costs one life. The game ends when all lives are lost.
5. **Earn Points**: Points are awarded for each obstacle avoided. Higher difficulty levels result in faster obstacles and greater scores.
6. **Restart or Quit**: Use the Restart button to replay with the same difficulty level, or Quit to exit the game.
   
## Project Structure

```plaintext
BlockGame/
│
├── main.py                 # Main game logic and Pygame interface
├── README.md               # Project information and instructions
└── requirements.txt        # (Optional) File for dependencies
