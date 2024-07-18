import threading
import concurrent.futures as cf
import time

#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(3)
        print('<-heavy_computing('+str(idx)+')')
        return idx, idx*idx

def start_threads(f, N):
    thList = []
    for i in range(N):
        th=threading.Thread(target=f, args=(i,))
        th.start()
        thList.append(th)
    return thList

def wait_threads(th_list):
    for th in th_list:
        th.join()

#Test software under this if        
if __name__ == "__main__":
    N=10

    print('None started')
    th_list=start_threads(heavy_computing, N)
    print('Wait...')
    ret=wait_threads(th_list)
    print('All futures completed')
    print(ret)
