import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 8080))
name = input("Pls input your name if you need answer")
sock.send(str.encode(name))

data = sock.recv(1024)
print(data.decode())

sock.close()