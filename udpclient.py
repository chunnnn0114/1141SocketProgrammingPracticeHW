import socket

SERVER_IP = "192.168.0.87"  # 伺服端 IP
PORT = 8888             # 必須與伺服端一致

# 建立 UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 傳送測試訊息給伺服端
msg = "Hello from client"
client.sendto(msg.encode(), (SERVER_IP, PORT))

# 接收伺服端的回覆
data, _ = client.recvfrom(1024)
print("Received from server:", data.decode())

# 關閉 socket
client.close()

