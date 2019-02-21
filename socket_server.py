from pynput import mouse
from pynput.mouse import Button, Controller
import socket
import json

mouse_controller = Controller()
from threading import Lock




def server_program():
    host = "10.6.16.18"
    port = 8080
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    # lock = Lock()
    while True:

        def on_move(x, y):
            cursor_position_string = json.dumps({"x": x, "y": y})
            import time
            time.sleep(.01)
            conn.send(cursor_position_string.encode())


        def on_click(x, y, button, pressed):
            print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))



        def on_scroll(x, y, dx, dy):
            print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

            # conn.send(x)


        with mouse.Listener(on_move=on_move, on_click=on_click,on_scroll=on_scroll) as listener:
            # print(dir(listener))
            # print(listener)
            # print("-----------------")
            listener.join()
        data = conn.recv(4800).decode()
        if not data or data != "ok":
            break
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
