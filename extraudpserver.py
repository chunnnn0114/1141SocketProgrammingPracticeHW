import socket
import hashlib
import random

# 定義一個函式來驗證資料的 checksum 是否正確
def verify_checksum(data, checksum):
    # 使用 MD5 演算法計算資料的雜湊值，並與封包中的 checksum 比對
    return hashlib.md5(data).hexdigest() == checksum

# 建立 UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 綁定 socket 到本機所有 IP 的 9999 port，準備接收封包
server.bind(('0.0.0.0', 9999))

# 儲存已成功接收的封包資料（以序號為 key）
received_packets = {}

# 記錄已看過的封包序號，用來隨機挑選要破壞的目標
all_seen_seqs = set()

# 記錄已經故意破壞過的封包序號，避免重複破壞
corrupted_once = set()

# 儲存目前這一輪要故意破壞的封包序號（每輪只挑一個）
corrupted_seq = None

print("Server started. Waiting for incoming packets...")  # 啟動提示

# 進入主迴圈，不斷接收封包
while True:
    # 接收封包（最大 1024 bytes），並取得來源位址
    packet, addr = server.recvfrom(1024)

    # 封包格式：
    # 前 4 bytes 是序號（整數）
    # 接著 32 bytes 是 checksum（MD5 雜湊值）
    # 剩下的是資料內容
    seq_num = int.from_bytes(packet[:4], 'big')     # 解析封包序號
    checksum = packet[4:36].decode()                # 解析 checksum 字串
    data = packet[36:]                              # 取得資料內容

    # 將目前收到的序號加入已看過的集合
    all_seen_seqs.add(seq_num)

    # 如果尚未指定本輪要破壞的封包，就從已看過的序號中隨機挑一個
    if corrupted_seq is None and all_seen_seqs:
        corrupted_seq = random.choice(list(all_seen_seqs))  # 隨機挑選一個序號
        print(f"Selected packet {corrupted_seq} to corrupt this round.")  # 顯示選擇結果

    # 如果當前封包是本輪指定要破壞的目標，且尚未破壞過，就故意破壞一次
    if seq_num == corrupted_seq and seq_num not in corrupted_once:
        print(f"Intentionally corrupting packet {seq_num}.")  # 顯示破壞動作
        data = b"corrupted_data"                              # 替換資料為錯誤內容
        corrupted_once.add(seq_num)                           # 標記為已破壞

    # 驗證 checksum 是否正確
    if verify_checksum(data, checksum):
        # 如果資料內容是 "END"，代表 Client 傳送結束訊號
        if data.decode() == "END":
            print("Received END signal. Transmission complete.")  # 顯示結束提示
            break  # 跳出主迴圈，結束程式

        # 顯示成功接收的封包內容
        print(f"Received packet {seq_num}: {data.decode()}")

        # 儲存封包資料
        received_packets[seq_num] = data

        # 傳送 ACK 回 Client，表示成功接收
        server.sendto(f"ACK{seq_num}".encode(), addr)
    else:
        # 如果驗證失敗，表示封包損毀，丟棄不處理
        print(f"Packet {seq_num} failed checksum. Discarded.")
