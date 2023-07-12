import socket

host = input("Enter server IP: ")

HOST = host
PORT = 12345
slidingWindow = 1 # sliding window initialized to 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connection Successful!\n")
    s.sendall("network".encode('UTF-8')) # Send initial string
    
    # msg = input("Client: ")
    # while msg != "quit":
    #     s.sendall(msg.encode())
    #     data = s.recv(1024)
    #     print(f"Server: " + data.decode())
    #     msg = input("Client: ")
    data = s.recv(1024)
    print(f"Server: " + data.decode('UTF-8'))
print("Connection Closed")


