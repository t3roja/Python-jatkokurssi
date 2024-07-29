import concurrent.futures as cf
import time

# Heavy computing for test purposes
def heavy_computing(idx):
    print('->heavy_computing(' + str(idx) + ')')
    time.sleep(3)
    print('<-heavy_computing(' + str(idx) + ')')
    return idx, idx * idx

def start_threads(f, N):
    futures = []
    with cf.ThreadPoolExecutor() as executor:
        for i in range(N):
            future = executor.submit(f, i)
            futures.append(future)
    return futures

def wait_threads(th_list):
    results = []
    for future in cf.as_completed(th_list):
        result = future.result()
        results.append(result)
    results.sort(key=lambda x: x[0])  # Sort results by idx to ensure the order
    return [res for _, res in results]

# Test software under this if        
if __name__ == "__main__":
    N = 10

    print('None started')
    th_list = start_threads(heavy_computing, N)
    print('Wait...')
    ret = wait_threads(th_list)
    print('All futures completed')
    print(ret)
