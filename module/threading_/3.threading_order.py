
import threading

main = threading.currentThread().getName()
print(main)

def snow():
    name = threading.currentThread().getName()
    print(name)

t1 = threading.Thread(target=snow)

t2 = threading.Thread(target=snow)

t3 = threading.Thread(target=snow)

t4 = threading.Thread(target=snow)

t4.start()
t3.start()


















