import multiprocessing

#share memory

def square_list(my_list,result,square_sum):
    for index,value in enumerate(my_list):
        result[index] = value * value

        square_sum.value = sum(result)

        # print result Array
        print("Result(in process p1): {}".format(result[:]))

        # print square_sum Value
        print("Sum of squares(in process p1): {}".format(square_sum.value))

if __name__ == '__main__':
    mylist = [1,2,3,4]

    #tao 1 mang kieu int 4 phan tu
    result = multiprocessing.Array('i',4)

    #create value of int data type
    square_sum = multiprocessing.Value('i')

    p1 = multiprocessing.Process(target=square_list,args=(mylist,result,square_sum))

    p1.start()
    p1.join()

    # print result array
    print("Result(in main program): {}".format(result[:]))

    # print square_sum Value
    print("Sum of squares(in main program): {}".format(square_sum.value))
