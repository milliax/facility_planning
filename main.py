import threading
import time
import sys
import signal
from visualizer import run_visualizer
from commander import run_commander, terminate_processes, vehicle_processes

def main():
    running = threading.Event()
    running.set()

    # Start the commander in a separate thread
    commander_thread = threading.Thread(target=run_commander,args=(running,))
    commander_thread.start()

    # signal handler for graceful exit
    def signal_handler(sig, frame):
        print("Exiting...")
        running.clear()
        terminate_processes(vehicle_processes)
        commander_thread.join()
        sys.exit(0)

    # Register signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # Start the visualizer in the main thread
    run_visualizer()


if __name__ == "__main__":
    main()
