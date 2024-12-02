import pygame
import sys
import zmq
import time
import signal

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
RED = (255, 0, 0)  # For undefined vehicles

# Set the dimensions of each grid cell
CELL_SIZE = 10

# Calculate the dimensions of the window
map_width = len(layout_map[0])
map_height = len(layout_map)
window_width = map_width * CELL_SIZE
window_height = map_height * CELL_SIZE

vehicles = []

print(f"Map dimensions: {map_width} x {map_height}")

# Create the window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Map Display")

# Initialize the font
pygame.font.init()
font = pygame.font.SysFont('Arial', 15)

# Set up the ZeroMQ connection
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "DISPATCH")
socket.setsockopt_string(zmq.SUBSCRIBE, "BROADCAST")
socket.setsockopt_string(zmq.SUBSCRIBE, "VEHICLE")

def render_time(screen,st):
    time_elapsed = time.time() - st
    text = font.render(f"Time Elapsed: {time_elapsed:.2f}", True, BLACK)
    text_rect = text.get_rect(center=(window_width // 2, window_height - 20))
    screen.blit(text, text_rect)

# Signal handler for graceful termination
def signal_handler(sig, frame):
    print('Terminating visualizer...')
    pygame.quit()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Main loop
def run_visualizer():
    global start_time
    start_time = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Receive messages from ZeroMQ
        try:
            message = socket.recv_string(flags=zmq.NOBLOCK)
            print(message)
            
            if message == "DISPATCH START":
                start_time = time.time()
                continue
            elif message.startswith("DISPATCH VEHICLE"):
                _, _,vehicle_id, color = message.split()
                vehicles.append((int(vehicle_id), color))
            
        except zmq.Again:
            pass  # No message received

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

        # Draw the vehicles
        for vehicle in vehicles:
            vehicle_id, color = vehicle
            x, y = layout_map[vehicle_id]

            vehicle_color_hex = dict(vehicle).get(id,'#FF0000').lstrip('#')
            vehicle_color = tuple(int(vehicle_color_hex[i:i+2], 16) for i in (0, 2, 4))


            # pygame.draw.rect(screen, int(color, 16), pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(screen, vehicle_color, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

        # Render the time
        render_time(screen, start_time)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()