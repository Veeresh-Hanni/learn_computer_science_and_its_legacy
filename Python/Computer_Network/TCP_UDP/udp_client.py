import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b"Hello UDP Server!", ("127.0.0.1", 65432))

data, addr = client_socket.recvfrom(2048)
print("Server says:", data.decode())

client_socket.close()
