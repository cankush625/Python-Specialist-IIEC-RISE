import socket

s = socket.socket()

ip = "192.168.43.34"
port = 1234

s.connect((ip, port))

s.recv(100)
s.send(b'Im client')
