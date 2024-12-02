import threading
import time
from visualizer import run_visualizer
from commander import run_commander

def main():
    # Start the visualizer in a separate thread
    visualizer_thread = threading.Thread(target=run_visualizer)
    visualizer_thread.start()

    # Start the commander in a separate thread
    commander_thread = threading.Thread(target=run_commander)
    commander_thread.start()

    # Wait for both threads to finish (optional)
    visualizer_thread.join()
    commander_thread.join()

if __name__ == "__main__":
    main()