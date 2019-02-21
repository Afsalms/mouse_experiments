
import socket
import json
from pynput.mouse import Button, Controller

mouse = Controller()



def client_program():
    host = "10.6.16.18"
    port = 8080

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = ""
    while message.lower().strip() != 'bye':
        data = client_socket.recv(4800).decode()
        print('Received from server: ' + data)
        json_data = json.loads(data)
        print(json_data)
        print("x: ", json_data["x"])
        print("y: ", json_data["y"])
        mouse.position = (json_data["x"], json_data["y"])
        client_socket.send("ok".encode())
    client_socket.close()


if __name__ == '__main__':
    client_program()
