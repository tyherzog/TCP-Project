import socket

host = input("Enter server IP: ")

HOST = host
PORT = 12345
slidingWindow = 1 # sliding window initialized to 1

def parseAck(data):
    msg = data.decode('UTF-8')
    if(msg[0:2] == "ACK" and len(msg) is 4):
        return int(msg[3], 10)
    else:
        return -1   # Parsed data is not an aknowledgement, return error

def slidingWindow(numPackets):
    pass

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