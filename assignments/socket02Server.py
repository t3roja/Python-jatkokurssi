import socket
import multiprocessing as mp
import threading as th
import socket
import time

localIP='127.0.0.1'
localPort=20001
buffSize=1024


def server_function(queue, client_address, UDPSocket, terminate_queue):
    count=0
    while True:
        in_msg=queue.get()
        if in_msg=='terminate':
            print('Insert '+str(client_address)+' to terminate queue.')
            terminate_queue.put(client_address)
            return
        
        count+=1
        
        out_msg='Got message "%s". Total count of messages is %d'%(in_msg, count)
        bytesToSend=str.encode(out_msg)
        UDPSocket.sendto(bytesToSend, client_address)

def terminate_thread(terminate_queue, client_list, client_lock):
    while True:
        a=terminate_queue.get()
        with client_lock:
            client_list.pop(a, None)
            print('Client '+str(a)+' removed.')
            print('%d active clients.'%(len(client_list)))

if __name__=='__main__':

    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPSocket.bind((localIP, localPort))

    print('UDP server up and listening')

    client_list={}
    client_lock=th.Lock()
    terminate_queue=mp.Queue()

    term_thread=th.Thread(target=terminate_thread, args=(terminate_queue, client_list, client_lock))
    term_thread.start()
    
    while True:
        bytesAddressPair = UDPSocket.recvfrom(buffSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        print(address, ':', message.decode())

        with client_lock:
            if not address in client_list.keys():
                queue=mp.Queue()
                ps=mp.Process(target=server_function, args=(queue, address, UDPSocket, terminate_queue))
                client_list[address]=(queue, ps)
                ps.start()
                print('Client '+str(address)+' added.')
                print('%d active clients.'%(len(client_list)))
            
            client_queue=client_list[address][0]
            
        client_queue.put(message.decode())

    
