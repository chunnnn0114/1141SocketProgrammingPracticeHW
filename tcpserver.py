import socket

HOST = "192.168.0.87"   # IP
PORT = 8888      # 使用的通訊埠(client和server的Port要一致)

# 建立 TCP socket (SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 綁定 IP 與 Port
server.bind((HOST, PORT))

# 開始監聽，最大等待連線數 = 1
server.listen(1)
print("TCP Server is running...")

# 接受客戶端連線 (阻塞等待)
conn, addr = server.accept()
print("Connected by", addr)

# 接收客戶端傳來的訊息
data = conn.recv(1024).decode()
print("Received from client:", data)

# 回覆客戶端訊息
reply = "Hello from server"
conn.sendall(reply.encode())

# 關閉連線
conn.close()
server.close()

# 確保結束時有訊息
print("TCP Server closed.")import socket

HOST = "192.168.0.87"   # IP
PORT = 8888      # 使用的通訊埠(client和server的Port要一致)

# 建立 TCP socket (SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 綁定 IP 與 Port
server.bind((HOST, PORT))

# 開始監聽，最大等待連線數 = 1
server.listen(1)
print("TCP Server is running...")

# 接受客戶端連線 (阻塞等待)
conn, addr = server.accept()
print("Connected by", addr)

# 接收客戶端傳來的訊息
data = conn.recv(1024).decode()
print("Received from client:", data)

# 回覆客戶端訊息
reply = "Hello from server"
conn.sendall(reply.encode())

# 關閉連線
conn.close()
server.close()
