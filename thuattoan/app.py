def timkiemtuyentinh(x,lst):
    for index, val in enumerate(lst):
        if lst[index] == x:
            print("{} in lst at index: {}".format(lst[index],index))

def timkiemnhiphan(x,lst):
    n = len(lst)
    mid = int(n/2)
    if x == lst[mid]:
        print("{} in lst at index: {}".format(lst[mid], mid))
    elif(x < lst[mid]):
        timkiemnhiphan(x,lst[0:mid])
    elif(x>lst[mid]):
        timkiemnhiphan(x,lst[mid:lst(n)])
    else:
        print("ko co")


def binary_search(array, target):
    low = 0
    mid = len(array) / 2
    upper = len(array)

    if len(array) == 1:
        if array[0] == target:
            print (target)
            return array[0]
        else:
            return False
    if target == array[mid]:
        print (array[mid])
        return mid
    else:
        if mid > low:
            arrayl = array[0:mid]
            binary_search(arrayl, target)

        if upper > mid:
            arrayu = array[mid:len(array)]
            binary_search(arrayu, target)

def bubblesort(lst):
    for passnum in range(len(lst)-1,0,-1):
        for i in range(passnum):
            if lst[i] > lst[i+1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

def selectionSort(lst):
    for passnum in range(len(lst)-1,0,-1):
        positionOfMax = 0

        for location in range(1,passnum+1):
            if lst[location]<lst[positionOfMax]:
                positionOfMax = location

        lst[passnum], lst[positionOfMax] = lst[positionOfMax], lst[passnum]

def insertSort(lst):
    for index in range(1,len(lst)):
        currentValue = lst[index]
        position = index

        while position > 0 and lst[position-1] > currentValue:
            lst[position] = lst[position-1]
            position = position-1
        lst[position] = currentValue

# quicksort
def partition(lst,first,last):
    num = lst[first]

    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while leftmark<=rightmark and lst[leftmark] <= num:
            leftmark = leftmark + 1
        while rightmark >= leftmark and lst[rightmark] >= num:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            lst[leftmark], lst[rightmark] = lst[rightmark], lst[leftmark]
    lst[first], lst[rightmark] = lst[rightmark], lst[leftmark]
    return rightmark

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def quickSort(lst):
    quickSortHelper(lst,0,len(lst)-1)

#merge sort
def merge_sort(x):

    if len(x) < 2:return x

    result,mid = [],int(len(x)/2)

    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result


if __name__ == '__main__':
    #timkiemtuyentinh(1,[1,4,2,1])
    l = [9,2,4,1,5,12,4]
    #timkiemnhiphan(3,l)
    merge_sort(l)
    print(merge_sort(l))