import socket

HOST = ""  # This should make it so that the server accepts any IP address
PORT = 12345
windowSize = 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Waiting for connection from a host...")
    # while msg != "quit":
    #     s.sendall(msg.encode())
    #     data = s.recv(1024)
    #     print(f"Server: " + data.decode())
    #     msg = input("Client: ")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected to ", str(addr))
        data = conn.recv(1024)
        if data.decode('UTF-8') is "network":
            msg = "ACK"
            conn.sendall(msg.encode('UTF-8'))
        # while data:
        #     print("Client: " + data.decode())
        #     msg = input("Server: ")
        #     conn.sendall(msg.encode())
        #     data = conn.recv(1024)
    print("Client has disconnected")
