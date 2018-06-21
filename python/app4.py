import multiprocessing

#server process

def print_records(records):
    """
    function to print record(tuples) in records(list)
    """
    for record in records:
        print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))


def insert_record(record, records):
    """
    function to add a new record to records(list)
    """
    records.append(record)
    print("New record added!\n")

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # create new list in server process memory
        records = manager.list([('sam',10),('cuong','14')])
        new_record = ('test',2)

        #create process
        p1 = multiprocessing.Process(target=insert_record,args=(new_record,records))
        p2 = multiprocessing.Process(target=print_records,args=(records,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()
