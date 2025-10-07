import socket

# 1️⃣ Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2️⃣ Bind to address and port
server_socket.bind(("127.0.0.1", 65432))

print("UDP Server listening...")

# 3️⃣ Receive data
while True:
    data, addr = server_socket.recvfrom(2048)
    print(f"Client says: {data.decode()}")

    # 4️⃣ Send a reply
    server_socket.sendto(b"Hello UDP Client!", addr)
