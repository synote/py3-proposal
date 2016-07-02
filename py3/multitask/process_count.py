import time
from multiprocessing import Process

def count_down(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    CNT = 1e8
    start = time.time()
    count_down(CNT)
    print(time.time() - start)

    start = time.time()
    t1 = Process(target=count_down, args = (5e7,))
    t2 = Process(target=count_down, args = (5e7,))
    t1.start();t2.start()
    t1.join();t2.join()
    print(time.time() - start)