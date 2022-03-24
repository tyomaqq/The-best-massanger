
import socket


server = socket.socket(


socket.AF_INET,

socket.SOCK_STREAM,


)


server.bind(
    
    
    ("127.0.0.1", 1234)
    
)

server.listen(5)


while True:
    user_socket, address =   server.accept()
    user_socket.send("You are connected".encode("utf-8"))