import pygame
import random
import string

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Block Game")

# Set up game variables
player_width = 50
player_height = 50
player_x = (width - player_width) // 2
player_y = height - player_height
player_speed = 3
lives = 3  # New lives system
high_score = 0

obstacle_width = 50
obstacle_height = 50
obstacle_speed = 1  # Default obstacle speed
obstacles = []  # List to hold multiple obstacles
score = 0
font = pygame.font.Font(None, 36)

# Button rectangles - initialize them once
start_button_rect = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 50)
quit_button_rect = pygame.Rect(width // 2 - 100, height // 2 + 130, 200, 50)
restart_button_rect = pygame.Rect(width // 2 - 100, height // 2 + 210, 200, 50)  # New restart button

# Function to show level selection
def show_level_selection():
    font_large = pygame.font.Font(None, 48)
    text_difficulty = font_large.render("Select Difficulty:", True, (0, 0, 0))
    window.blit(text_difficulty, (width // 2 - 170, height // 2))

    font_medium = pygame.font.Font(None, 36)
    text_easy = font_medium.render("1: Easy", True, (0, 0, 0))
    window.blit(text_easy, (width // 2 - 60, height // 2 + 60))

    text_medium = font_medium.render("2: Medium", True, (0, 0, 0))
    window.blit(text_medium, (width // 2 - 70, height // 2 + 100))

    text_hard = font_medium.render("3: Hard", True, (0, 0, 0))
    window.blit(text_hard, (width // 2 - 45, height // 2 + 140))

# Function to set obstacle speed based on level
def set_obstacle_speed(level):
    global obstacle_speed
    if level == 1:  # Easy
        obstacle_speed = 1
    elif level == 2:  # Medium
        obstacle_speed = 3
    elif level == 3:  # Hard
        obstacle_speed = 5

# Function to start or restart the game
def start_game(level):
    global score, lives, obstacles, game_active
    set_obstacle_speed(level)  # Set obstacle speed according to level
    score = 0
    lives = 3
    obstacles.clear()  # Reset obstacles
    game_active = True
    # Create initial obstacles based on the set difficulty
    for _ in range(3):  # Start with 3 obstacles
        obstacles.append(create_obstacle())

# Function to create a new obstacle
def create_obstacle():
    x = random.randint(0, width - obstacle_width)
    y = random.randint(-300, -obstacle_height)
    speed = random.randint(obstacle_speed, obstacle_speed + 2)  # Speed varies around level speed
    return {"x": x, "y": y, "speed": speed}

# Function to draw a button
def draw_button(text, rect, color, text_color):
    pygame.draw.rect(window, color, rect)
    font_button = pygame.font.Font(None, 36)
    button_text = font_button.render(text, True, text_color)
    text_rect = button_text.get_rect(center=rect.center)
    window.blit(button_text, text_rect)

# Function to display the menu
def show_menu():
    font_large = pygame.font.Font(None, 48)
    text_title = font_large.render("Block Game", True, (0, 0, 0))
    window.blit(text_title, (width // 2 - 120, height // 2 - 200))

    draw_button("Start New Game", start_button_rect, (0, 255, 0), (0, 0, 0))
    draw_button("Quit Game", quit_button_rect, (255, 0, 0), (0, 0, 0))
    
    # Show restart button if the game has been played before
    if score > 0 or lives < 3:
        draw_button("Restart Game", restart_button_rect, (0, 0, 255), (255, 255, 255))

# Game loop
running = True
level_selected = False
level = 1
game_active = False
showing_menu = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not level_selected:
                if event.key == pygame.K_1:
                    level = 1
                    level_selected = True
                elif event.key == pygame.K_2:
                    level = 2
                    level_selected = True
                elif event.key == pygame.K_3:
                    level = 3
                    level_selected = True

        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not level_selected and not game_active:
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    start_game(level)
                    showing_menu = False
                elif quit_button_rect.collidepoint(mouse_x, mouse_y):
                    running = False
                elif restart_button_rect.collidepoint(mouse_x, mouse_y):  # Restart button click handling
                    start_game(level)
                    showing_menu = False
            elif showing_menu:
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    start_game(level)
                    showing_menu = False
                elif quit_button_rect.collidepoint(mouse_x, mouse_y):
                    running = False
                elif restart_button_rect.collidepoint(mouse_x, mouse_y):  # Restart button click handling
                    start_game(level)
                    showing_menu = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Update game objects
    if game_active:
        for obstacle in obstacles:
            obstacle["y"] += obstacle["speed"]
            if obstacle["y"] > height:
                obstacle["x"] = random.randint(0, width - obstacle_width)
                obstacle["y"] = -obstacle_height
                obstacle["speed"] = random.randint(obstacle_speed, obstacle_speed + 2)
                score += 1

        # Check for collisions with obstacles
        for obstacle in obstacles:
            if obstacle["y"] + obstacle_height > player_y and obstacle["y"] < player_y + player_height:
                if obstacle["x"] + obstacle_width > player_x and obstacle["x"] < player_x + player_width:
                    lives -= 1
                    obstacle["y"] = -obstacle_height  # Reset the obstacle position
                    if lives <= 0:
                        game_active = False
                        showing_menu = True
                        high_score = max(high_score, score)  # Update high score

    # Draw game objects
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 255), (player_x, player_y, player_width, player_height))
    for obstacle in obstacles:
        pygame.draw.rect(window, (255, 0, 0), (obstacle["x"], obstacle["y"], obstacle_width, obstacle_height))

    # Display score, lives, and high score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
    high_score_text = font.render(f"High Score: {high_score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))
    window.blit(lives_text, (10, 50))
    window.blit(high_score_text, (10, 90))

    # Show level selection if it's not selected yet
    if not level_selected and not game_active:
        show_level_selection()
    elif showing_menu:
        show_menu()

    # Update the screen
    pygame.display.update()
    clock.tick(60)

# Clean up Pygame
pygame.quit()
