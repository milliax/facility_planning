import zmq
import sys

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

status = {
    "current_position": {
        "x": 0,
        "y": 0,
    },
    "current_direction": "N",
}

vehicle_id = sys.argv[1]

# connection setup
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5555")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "DISPATCH")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "VEHICLE")

pusher = context.socket(zmq.PUSH)
pusher.connect("tcp://localhost:5556")

# choose the initial position
responsible_row = {
    "start": sys.argv[2],
    "end": sys.argv[3]
}

initial_position = {
    "x": 20,
    "y": 20,
}

status["current_position"]["x"] = initial_position["x"]
status["current_position"]["y"] = initial_position["y"]
print(f"Vehicle {vehicle_id} is initialized at {initial_position['x']}, {initial_position['y']}")

while True:
    # 處理任務的執行過程，模擬移動和狀態更新

    # send_message = f"VEHICLE POSITION {vehicle_id} {status["current_position"]['x']} {status["current_position"]['y']} {status["current_direction"]}"
    send_message = f"VEHICLE POSITION {vehicle_id} {status["current_position"]["x"]} {status['current_position']['y']} {status["current_direction"]}"
    # print(send_message)
    pusher.send_string(send_message)


