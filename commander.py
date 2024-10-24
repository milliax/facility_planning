import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# 模擬派發任務
tasks = [("start1", "end1"), ("start2", "end2")]

while True:
    for task in tasks:
        message = f"DISPATCH {task[0]} {task[1]}"
        socket.send_string(message)
    time.sleep(1)  # 每秒派發一次任務