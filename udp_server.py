# udp_server.py
import socket

HOST = "0.0.0.0"   # 監聽所有網卡
PORT = 9999          # 建議不要跟 TCP 共用同一個 port，改成 9999 比較清楚

# 建立 UDP socket (SOCK_DGRAM)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 綁定 IP 與 Port
server.bind((HOST, PORT))
print("UDP Server is running...")

# 接收來自客戶端的訊息 (回傳值有 data 和來源地址 addr)
data, addr = server.recvfrom(1024)
print(f"Connected by {addr}")       # 顯示誰傳資料來
print("Received from client:", data.decode())

# 回覆訊息給客戶端
reply = "Hello from server"
server.sendto(reply.encode(), addr)
print("Sent to client:", reply)     # 顯示已經回覆什麼

# UDP 是無連線協定，用完就可以關閉
server.close()

print("UDP Server closed.")         # 提示程式結束
