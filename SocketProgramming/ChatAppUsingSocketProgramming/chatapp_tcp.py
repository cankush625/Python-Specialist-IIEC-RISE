import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Enter your IP address: ")
port = int(input("Enter the port number: "))

s.bind((ip, port))

s.listen()

# session_info = s.accept()
connection, address = s.accept()

connection.send('hello'.decode())
data = connection.recv(1024)

connection.close()
