import zmq
import time
import subprocess

# configurations

from layout import FROM_TO_CHART


num_vehicle = 2

""" Defining functions """

def terminate_processes(processes):
    for process in processes:
        process.terminate()

# create connection
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# create layout
layout_process = subprocess.Popen(["python", "layout.py"])

# create vehicles
vehicle_processes = []

for i in range(num_vehicle):
    process = subprocess.Popen(["python", "vehicle.py"])
    vehicle_processes.append(process)

# 模擬派發任務
tasks = [("start1", "end1"), ("start2", "end2")]



while True:
    for task in tasks:
        message = f"DISPATCH {task[0]} {task[1]}"
        socket.send_string(message)
    time.sleep(1)  # 每秒派發一次任務