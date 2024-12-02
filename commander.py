import zmq
import time
import subprocess
import sys
import signal
import threading

# configurations

num_vehicle = 2
vehicle_processes = []

""" Defining functions """

colors = [
    "FFFBEB",
    "FEF3c7",
    "FDE68A",
    "FCD34D",
    "FBBF24",
    "F59E0B",
    "FEFCE8",
    "FEF9C3",
    "FEF08A",
    "FDE047",
    "FACC15",
    "EAB308",
]


def terminate_processes(processes):
    for process in processes:
        process.terminate()
    for process in processes:
        process.wait()


# Signal handler for graceful exit
def signal_handler(sig, frame):
    print("Terminating processes...")
    terminate_processes()
    sys.exit(0)

def read_output(process):
    for line in process.stdout:
        print(line, end='')

signal.signal(signal.SIGINT, signal_handler)

def run_commander(running):
    global vehicle_processes
    # create connection
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5555")

    puller = context.socket(zmq.PULL)
    puller.bind("tcp://*:5556")

    publisher.send_string("BROADCAST COMMANDER initialized")

    for i in range(num_vehicle):
        process = subprocess.Popen(
            ["python", "vehicle.py", str(i),"A","Z"],)
        vehicle_processes.append(process)
        # threading.Thread(target=read_output, args=(process,), daemon=True).start()

    # give time for vehicles to connect
    time.sleep(1)

    # send vehicle information to visualizer

    for i in range(num_vehicle):
        publisher.send_string(f"DISPATCH VEHICLE {i} {colors[i]}")

    # send start signal to visualizer

    publisher.send_string("DISPATCH START")

    # keep alive to handle signals
    while running.is_set():
        response = puller.recv_string()
        # print(f"Received: {response}")
        publisher.send_string(response)

    print("Terminating commander...")
    terminate_processes(vehicle_processes)
