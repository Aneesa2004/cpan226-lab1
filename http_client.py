# http_client.py
# Student Name: Aneesa
# CPAN-226 Lab 1

from socket import *

# Server info
server_name = 'gaia.cs.umass.edu'
server_port = 80

# 1. Create TCP socket (IPv4, TCP)
client_socket = socket(AF_INET, SOCK_STREAM)

# 2. Connect to server
client_socket.connect((server_name, server_port))

# 3. Prepare HTTP request
request = "GET /kurose_ross/interactive/index.php HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\nConnection: close\r\n\r\n"

# 4. Send request
client_socket.send(request.encode())

# 5. Receive response (up to 4096 bytes)
response = client_socket.recv(4096)

# 6. Print response
print(response.decode())

# 7. Close socket
client_socket.close()
