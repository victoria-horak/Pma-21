import socket
sock = socket.socket()
sock.bind(('', 8080))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    line = "Hello, " + data.decode()
    conn.send(str.encode(line))
conn.close()
