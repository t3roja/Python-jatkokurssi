import socket

localIP="127.0.0.1"
localPort=20002
buffSize=1024

TCPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
TCPSocket.bind((localIP, localPort))
print("TCP server up and listening")

while True :
    TCPSocket.listen()
    conn, addr=TCPSocket.accept()

    print(f"Connected by {addr}")
    socket_open=True
    while socket_open:
            data=conn.recv(buffSize)
            if not data:
                socket_open=False
            else:
                print("Got message:", data)
                msg="Hello UDP Client\n"
                print("send:", msg)
                conn.sendall(msg.encode())
                print("send:", data.decode())
                conn.sendall(data)

