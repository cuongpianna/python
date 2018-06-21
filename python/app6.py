import multiprocessing

#ham nay sai

def withdraw(ballace):
    for _ in range(10000):
        ballace.value = ballace.value - 1

def deposit(ballance):
    for _ in range(10000):
        ballance.value = ballance.value + 1

def perform_transactions():
    #init ballance in memory
    balance = multiprocessing.Value('i',100)

    p1 = multiprocessing.Process(target=withdraw,args=(balance,))
    p2 = multiprocessing.Process(target=deposit,args=(balance,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final ballace = {}".format(balance.value))


if __name__ == "__main__":
    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions()