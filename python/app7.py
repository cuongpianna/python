import multiprocessing
import os

""""
module using Lock obj quan ly truy cap du lieu

"""

def withdraw(balance,lock):
    for _ in range(10000):
        lock.acquire()
        balance.value= balance.value - 1
        lock.release()

def deposit(banalce,lock):
    for _ in range(10000):
        lock.acquire()
        banalce.value = banalce.value + 1
        lock.release()

def perform_tracsaction():
    balance = multiprocessing.Value('i',100)

    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=withdraw,args=(balance,lock))
    p2 = multiprocessing.Process(target=deposit,args=(balance,lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Final process of {}: {}'.format(os.getpid(),balance.value))

if __name__ == '__main__':
    for i in range(10):
        perform_tracsaction()