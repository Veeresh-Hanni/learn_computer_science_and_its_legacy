import socket

# Create socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to host and port
server_socket.bind(("127.0.0.1", 65432))

# Listen for connections
server_socket.listen()

print("Server is listening...")

# Accept client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data
data = conn.recv(1024).decode()
print("Client says:", data)

# Send response
conn.sendall("Hello from Server!".encode())

# Close connection
conn.close()
