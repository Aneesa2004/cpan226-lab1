# http_client_ssl.py
# Student Name: Aneesa
# Student id: n01745842

import ssl
from socket import *

# Server info
server_name = 'gaia.cs.umass.edu'
server_port = 443  # HTTPS port

# 1. Create TCP socket (IPv4, TCP)
client_socket = socket(AF_INET, SOCK_STREAM)

# 2. Wrap socket with SSL using a default context
context = ssl.create_default_context()
ssl_socket = context.wrap_socket(client_socket, server_hostname=server_name)

# 3. Connect to server
ssl_socket.connect((server_name, server_port))

# 4. Prepare HTTP request
request = "GET /kurose_ross/interactive/index.php HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\nConnection: close\r\n\r\n"

# 5. Send request
ssl_socket.send(request.encode())

# 6. Receive response (up to 4096 bytes)
response = ssl_socket.recv(4096)

# 7. Print response
print(response.decode())

# 8. Close socket
ssl_socket.close()



