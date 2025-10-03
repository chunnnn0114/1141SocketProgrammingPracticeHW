import socket

HOST = "192.168.0.87"   # 監聽所有網路介面
PORT = 8888        # 使用的通訊埠(要與client一樣)

# 建立 UDP socket (SOCK_DGRAM)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 綁定 IP 與 Port
server.bind((HOST, PORT))
print("UDP Server is running...")

# 接收來自客戶端的訊息 (回傳值有 data 和來源地址 addr)
data, addr = server.recvfrom(1024)
print("Received from client:", data.decode())

# 回覆訊息給客戶端
reply = "Hello from server"
server.sendto(reply.encode(), addr)

# UDP 是無連線協定，用完就可以關閉
server.close()
