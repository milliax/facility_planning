import zmq

# configuration

vehicle = {
    "speed": 0.5, # 0.5 m/sec
    "stop_time": 2, # 2 sec to stop at each node
    "spin_time": 3, # 3 sec to make a turn
    "precise_align": 5,  # 5 sec to make a precise alignment
    "grapping_time": 35,  # 35 sec to grap an object
    "charging_time": 60*60,  # 1 hour to charge the battery
    "battery_capacity": 60*60*4,  # 4 hours of battery capacity

    "slot_number": 3,  # 3 slots for objects

    "current_battery_level": 60*60*4,  # 4 hours of battery capacity started with full charged
}

# connection setup
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "DISPATCH")

while True:
    message = socket.recv_string()
    command, start, end = message.split()
    # 處理任務的執行過程，模擬移動和狀態更新
    print(f"Vehicle moving from {start} to {end}")