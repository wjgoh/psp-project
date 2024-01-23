import pygame
import keyboard

# Initialize Pygame
pygame.init()

# Set up the game window
s_width, s_height = 800, 600
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Maze Example")

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define maze layout (0 represents an open space, 1 represents a wall)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0 , 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Calculate cell size based on screen size and maze dimensions
cell_width = s_width // len(maze[0])
cell_height = s_height // len(maze)

# Load the character image (smaller size)
char_img = pygame.Surface((cell_width // 2, cell_height // 2))
char_img.fill(red)
char_rect = char_img.get_rect()

# Set the initial position of the character
char_rect.x = cell_width
char_rect.y = cell_height

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Set the game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the character
    if keyboard.is_pressed('left'):
        if maze[char_rect.y // cell_height][(char_rect.x - 5) // cell_width] == 0:
            char_rect.x -= 5
    if keyboard.is_pressed('right'):
        if maze[char_rect.y // cell_height][(char_rect.x + char_rect.width + 5) // cell_width] == 0:
            char_rect.x += 5
    if keyboard.is_pressed('up'):
        if maze[(char_rect.y - 5) // cell_height][char_rect.x // cell_width] == 0:
            char_rect.y -= 5
    if keyboard.is_pressed('down'):
        if maze[(char_rect.y + char_rect.height + 5) // cell_height][char_rect.x // cell_width] == 0:
            char_rect.y += 5

    # Update the screen
    screen.fill(white)

    # Draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, black, (col * cell_width, row * cell_height, cell_width, cell_height))
    
    # Draw the character
    screen.blit(char_img, char_rect)

    pygame.display.flip()

# Quit the game
pygame.quit()