import socket


SERVER_HOST = 'localhost'
SERVER_PORT = 8080

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    response = 'HTTP/1.0 200 OK\n\nHello World'
    if request.split()[0] == 'GET':
        response = 'HTTP/1.0 200 OK\n\nHello User'
    elif request.split()[0] == 'POST':
        user_name = request.split()[-2]
        response = 'HTTP/1.0 200 OK\n\nHello ' + user_name
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()