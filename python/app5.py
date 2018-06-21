import multiprocessing

"""
module share memory using Queue
"""

def square_list(mylist,q):
    """
    function to square a given list
    :param mylist: list
    :param q: queue
    :return: None
    """
    #append list to queue
    for num in mylist:
        q.put(num * num)

def print_queue(q):
    print("Queue elements")
    while not q.empty():
        print(q.get())
    print('Q is now empty')

if __name__ == '__main__':
    mylist = [1,2,3]

    #create q
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=square_list,args=(mylist,q))
    p2 = multiprocessing.Process(target=print_queue,args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()