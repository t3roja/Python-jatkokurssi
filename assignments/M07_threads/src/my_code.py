import threading
import concurrent.futures as cf
import time

count = 0


def external_function():
    global count
    count += 1


def external_count():
    global count
    return count

#Sample function for test purposes
def computing5s(thr_id):
    time.sleep(1)
    external_function()
            
    return thr_id, thr_id*thr_id


def init_values(f):

    """
        for i in range(50):
        idx, val=f(i)
        f_values[idx]=val
    """
def init_values(f):
    f_values = {}
    with cf.ProcessPoolExecutor() as executor:
        futures = {executor.submit(f, i): i for i in range(50)}
        for future in cf.as_completed(futures):
            idx = futures[future]
            try:
                _, val = future.result()
                f_values[idx] = val
            except Exception as e:
                print(f"Thread {idx} generated an exception: {e}")
    return f_values


#Test software under this if        
if __name__ == "__main__":
    ret=init_values(computing5s)
    print(ret)

