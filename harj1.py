from time import sleep
import threading

counter=0
counter_lock=threading.Lock()

def thread_func(msg, idx):
    sleep(0.01)
    global counter
    with counter_lock:
        counter=counter+1
        print(idx, counter)
        
    print(idx, msg)

th_list=[]

for i in range(100):
    th=threading.Thread(target=thread_func, args=('Hello from thread '+str(i), i))
    th.start()
    th_list.append(th)

for th in th_list:
    th.join()

