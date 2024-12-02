import zmq
import time
import subprocess

# configurations

num_vehicle = 2

""" Defining functions """

def terminate_processes(processes):
    for process in processes:
        process.terminate()

# create connection
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# create vehicles
vehicle_processes = []

for i in range(num_vehicle):
    process = subprocess.Popen(["python", "vehicle.py"])
    vehicle_processes.append(process)

