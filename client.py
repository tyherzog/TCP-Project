import socket

host = input("Enter server IP: ")

HOST = host
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connection Successful!\nStart chatting with your partner")
    msg = input("Client: ")
    while msg != "quit":
        bmsg = bytes(msg, 'utf-8')
        s.sendall(bmsg)
        data = s.recv(1024)
        print(f"Server: {data!r}")
        msg = input("Client: ")

print("Connection Closed")