import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "DISPATCH")

while True:
    message = socket.recv_string()
    command, start, end = message.split()
    # 處理任務的執行過程，模擬移動和狀態更新
    print(f"Vehicle moving from {start} to {end}")