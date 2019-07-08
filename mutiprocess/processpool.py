import multiprocessing as ms
import time
import random
import psutil
import os


def test(i):
    t_start = time.time()
    print("%d开始执行第%d个任务" % (os.getpid(),i))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("%d执行完第%d个任务，耗时%.2f" % (os.getpid(),i,t_stop - t_start))

if __name__ == '__main__':
    pool = ms.Pool(processes=6)
    for i in range(0,30):
        pool.apply_async(test,(i,))
    pool.close()
    pool.join()

























