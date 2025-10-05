import socket

SERVER_IP = "192.168.0.87"  # 伺服端 IP (如果跨電腦，改成伺服端的 IP)
PORT = 8888 # 必須跟伺服端一致

# 建立 TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 程式啟動提示
print("TCP Client is running...")  

# 嘗試連線到伺服端
client.connect((SERVER_IP, PORT))

# 傳送測試訊息
msg = "Hello from client"
client.sendall(msg.encode())

# 接收伺服端的回覆
data = client.recv(1024).decode()
print("Received from server:", data)

# 關閉連線
client.close()

# 程式結束提示
print("TCP Client closed.") 

SERVER_IP = "192.168.0.87"  # 伺服端 IP (如果跨電腦，改成伺服端的 IP)
PORT = 8888 # 必須跟伺服端一致

# 建立 TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 嘗試連線到伺服端
client.connect((SERVER_IP, PORT))

# 傳送測試訊息
msg = "Hello from client"
client.sendall(msg.encode())

# 接收伺服端的回覆
data = client.recv(1024).decode()
print("Received from server:", data)

# 關閉連線
client.close()
