import socket
import hashlib

# 建立 UDP socket 並設定 timeout（1 秒）
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(1)

# 封包格式：序號 + checksum + 資料
def create_packet(seq_num, data):
    checksum = hashlib.md5(data.encode()).hexdigest()  # 計算 MD5 checksum
    return seq_num.to_bytes(4, 'big') + checksum.encode() + data.encode()

# 要傳送的資料列表
data_list = ["Hello", "this", "is", "reliable", "UDP test"]

# Server 的 IP 和 port（請改成你 Server 電腦的 IP）
server_addr = ('192.168.0.87', 9999)

# 傳送每筆資料
for i, msg in enumerate(data_list):
    packet = create_packet(i, msg)  # 建立封包
    while True:
        client.sendto(packet, server_addr)  # 傳送封包
        try:
            ack, _ = client.recvfrom(1024)  # 等待 ACK
            if ack.decode() == f"ACK{i}":
                print(f"Packet {i} acknowledged.")  # 成功收到 ACK
                break
        except socket.timeout:
            print(f"Timeout on packet {i}. Resending...")  # 逾時重送

# 傳送結束封包
end_packet = create_packet(9999, "END")  # 使用特殊序號 9999 表示結束
client.sendto(end_packet, server_addr)
print("All packets sent. Transmission complete.")  # 顯示結束提示
