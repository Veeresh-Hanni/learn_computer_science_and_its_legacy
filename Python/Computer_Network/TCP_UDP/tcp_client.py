import socket

# Create socket (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("127.0.0.1", 65432))

# Send message
client_socket.sendall("Hello Server!".encode())

# Receive reply
data = client_socket.recv(1024).decode()
print("Server says:", data)

client_socket.close()
