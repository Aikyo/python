from multiprocessing import Pool
from threading import Thread

from multiprocessing import Process

def loop():
    while True:
        pass

if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=loop)
        t.start()















