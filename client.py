


import socket
socket.client = socket.socket(
socket.AF_INET,
socket.SOCK_STREAM,
)
socket.client.connect(
     ("127.0.0.1", 1234)
)
while True:
    data = socket.client.recv(2048)
    print(data.decode("utf-8"))