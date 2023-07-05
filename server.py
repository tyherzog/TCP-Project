import socket

HOST = ""  # This should make it so that the server accepts any IP address
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected to {addr}")
        data = conn.recv(1024)
        while data:
            print(f"Client: {data!r}")
            msg = input("Server: ")
            bmsg = bytes(msg, 'utf-8')
            conn.sendall(bmsg)
            data = conn.recv(1024)
    print("Client has disconnected")
