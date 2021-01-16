import socket
import threading

# By default, socket uses tcp protocol
s = socket.socket()
# Making the socket reusable again
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = ""
port = 1234

s.bind(( ip, port ))
s.listen()

def conn():
    print(addr)
    c.send(b'Im server')
    data = c.recv(100)
    print(data)

while True:
    c, addr = s.accept()
    t = threading.Thread(
            target = conn,
            args = (c, addr)
            )
    t.start()
