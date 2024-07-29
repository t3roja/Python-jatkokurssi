import socket
import sys
import threading as th
import random

localIP="127.0.0.1"
serverPort=7537
buffSize=1024
maxClients = 25

def handleClient(conn, addr, clientCount):
    print("Client ", addr, " connected")
    nums = []

    while True:
        data = conn.recv(buffSize)
        if not data:
            break
        
        msg = data.decode()
        print("Message from ", addr, " : ", msg)
        nums.append(int(msg))

        totalSum = sum(nums)
        conn.sendall(str(totalSum).encode())

    print("Connection with client ", addr, " terminated. Sent :", totalSum)
    conn.close()

    with clientLock:
        clientCount += 1
        if clientCount >= maxClients:
            TCPSocket.close()

if __name__ == '__main__':

    TCPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    TCPSocket.bind((localIP, serverPort))
    TCPSocket.listen()

    print("TCP server listenig to port", serverPort)

    clientList = {}
    clientCount = 0
    clientLock = th.Lock()

    while True:

        conn, addr = TCPSocket.accept()
        clientThread = th.Thread(target=handleClient, args=(conn, addr, clientCount))
        clientThread.start()


        
"""
    #You can utilize following client for test purposes
    def client_main():
        TCPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        TCPSocket.connect((localIP, serverPort))

        rnd=random.sample(range(-30, 30), 5)
        for r in rnd:
            msg=str(r)
            print('Send:', msg)
            bytesToSend=str.encode(msg)

            TCPSocket.send(bytesToSend)

            #print('Wait message')
            data=TCPSocket.recv(buffSize)
            data=data.decode()
            data=data.splitlines()
            msg1=data[0]
            print('Received:', msg1)

        print('Close socket')
        TCPSocket.close()

        print('Got sum:'+msg1+'. Value shall be '+str(sum(rnd))+', sent data='+str(rnd))
        
        assert int(msg1)==sum(rnd)
        print('Test passed!')



    #Set True to run the clients
    run_client=False

    if run_client:
        th_list=[]
        for i in range(20):
            th_list.append(threading.Thread(target=client_main))
            th_list[-1].start()

        for th in th_list:
            th.join()

        for i in range(5):
            th_list.append(threading.Thread(target=client_main))
            th_list[-1].start()

        for th in th_list:
            th.join()


        #After 25 clients the server shall exit"""
