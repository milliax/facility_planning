import pygame
import sys

from layout import layout_map, generate_map

# Initialize Pygame
pygame.init()
# Generate the map
generate_map()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)

# Set the dimensions of each grid cell
CELL_SIZE = 20

# Calculate the dimensions of the window
map_width = len(layout_map[0])
map_height = len(layout_map)
window_width = map_width * CELL_SIZE
window_height = map_height * CELL_SIZE

# Create the window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Map Display")

# Main loop
def run_visualizer():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the map
        for y, row in enumerate(layout_map):
            for x, cell in enumerate(row):
                color = WHITE
                if cell == 0:
                    color = BLACK
                elif cell == 1:
                    color = GRAY
                elif cell == 3:
                    color = BLUE
                pygame.draw.rect(screen, color, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()