from multiprocessing import Pool
from multiprocessing import Process

def loop():
    while True:
        pass


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=loop)
        p.start()















