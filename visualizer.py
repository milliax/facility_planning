import pygame
import sys
import zmq
import time
import signal

from layout import layout_map, generate_map, gap, ROWS

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

vehicle_colors = []
vehicle_positions = {}

print(f"Map dimensions: {map_width} x {map_height}")

# Create the window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Map Display")

# Initialize the font
pygame.font.init()
font = pygame.font.SysFont("Arial", 15)

# Set up the ZeroMQ connection
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "DISPATCH")
socket.setsockopt_string(zmq.SUBSCRIBE, "BROADCAST")
socket.setsockopt_string(zmq.SUBSCRIBE, "VEHICLE")


def render_time(screen, st):
    time_elapsed = time.time() - st
    text = font.render(f"Time Elapsed: {time_elapsed:.2f}", True, BLACK)
    text_rect = text.get_rect(center=(window_width // 2, window_height - 20))
    screen.blit(text, text_rect)


def render_text(screen, text, x, y):
    text = font.render(text, True, BLACK)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


# Signal handler for graceful termination
def signal_handler(sig, frame):
    print("Terminating visualizer...")
    pygame.quit()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


# Main loop
def run_visualizer():
    global start_time
    global vehicle_colors
    global vehicle_positions

    start_time = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Receive messages from ZeroMQ
        try:
            message = socket.recv_string(flags=zmq.NOBLOCK)
            # print(message)

            if message == "DISPATCH START":
                print("Starting the timer")
                start_time = time.time()
                continue
            elif message.startswith("DISPATCH VEHICLE"):
                print(message)
                _, _, vehicle_id, color = message.split()
                vehicle_colors.append((vehicle_id, color))
            elif message.startswith("VEHICLE POSITION"):
                _, _, vehicle_id, x, y, direction = message.split()
                vehicle_positions[vehicle_id] = {
                    "x": int(x),
                    "y": int(y),
                    "direction": direction,
                }

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
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )

        # put the row letters on the map according to the layout and the gap

        gap_aggregation = -1
        for (tag,g) in zip(ROWS,gap):
            gap_aggregation += g
            gap_aggregation += 1
            render_text(screen, tag, (gap_aggregation + 1) * CELL_SIZE, 15)

        # Draw the vehicles
        for vehicle in vehicle_colors:
            id, color = vehicle

            if id not in vehicle_positions:
                print(f"Vehicle {id} not found in vehicle_positions")
                continue

            vehicle_color_hex = color.lstrip("#")
            vehicle_color = tuple(
                int(vehicle_color_hex[i : i + 2], 16) for i in (0, 2, 4)
            )

            # pygame.draw.rect(screen, int(color, 16), pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(
                screen,
                vehicle_color,
                (
                    vehicle_positions[id]["x"] * CELL_SIZE + CELL_SIZE // 2,
                    vehicle_positions[id]["y"] * CELL_SIZE + CELL_SIZE // 2,
                ),
                CELL_SIZE // 2,
            )

        # Render the time
        render_time(screen, start_time)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()
