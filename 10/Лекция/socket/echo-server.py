# echo-server.py

import socket

HOST = "127.0.0.1" # (localhost)
PORT = 1024  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # socket.SOCK_DGRAM - UDP socket
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.sendall(data)