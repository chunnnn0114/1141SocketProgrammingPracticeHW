# udp_client.py
import socket

SERVER_IP = "172.20.10.3"  # 伺服端 IP
PORT = 9999              # 必須與伺服端一致 (建議改成和 TCP 不同的 port)

# 建立 UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 提示開始
print("UDP Client is running...")   

# 傳送測試訊息給伺服端
msg = "Hello from client"
client.sendto(msg.encode(), (SERVER_IP, PORT))
print("Sent to server:", msg)

# 接收伺服端的回覆
data, _ = client.recvfrom(1024)
print("Received from server:", data.decode())

# 關閉 socket
client.close()

# 提示結束

print("UDP Client closed.")  
