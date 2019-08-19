import numpy as np

#length = int(input ('give me the number of elements for your cool array : '))
#array = list()*length
N=100
array = [np.random.randint(0,100) for i in range(N)]
array1 = [[np.random.randint(0,100)] for i in range(N)]
length = len(array)
"""
for i in range( length):
 print('give me the element', i+1)
 member = int(input(':'))
 array.append([member])
#cool=[]
"""
#print( array)



def my_interval(first , last ,step):
    while first <=last :
         yield first
         first += step



def two_sort(array):
    if length % 2 == 0:

        for j in my_interval(0,length-1,2):
            if array[j ]>array[j+1]:
                swap  = array[j]
                array[j] = array[j+1]
                array[j+1]  = swap
    else :
        for j in my_interval(0,length-2,2):
            if array[j ]>array[j+1]:
                swap  = array[j]
                array[j] = array[j+1]
                array[j+1]  = swap


    return array


def merge(a, b):
    """ Merge of two sorted arrays (iterative version)

    IN:  sorted arrays a and b
    OUT: merging of a and b into one sorted array
    """
    if not a or not b or a[-1] < b[0]:
        return a + b
    res = [ a[0] for i in range(len(a)+len(b)) ]
    next_a = 0
    last_a = len(a)-1
    last_b = len(b)-1
    for i in range(len(res)):
        next_b = i - next_a
        if (next_a > last_a) or ((next_b <= last_b) and (a[next_a] > b[next_b])):
            res[i] = b[next_b]
        else:
            res[i] = a[next_a]
            next_a += 1
    return res
#merge sorting 
def my_sort(array):
    if len(array) == 1:
        return array
    return merge(my_sort(array[:len(array)//2]),my_sort(array[len(array)//2:]))
#merge sorting bottom to top 
def sorty (array):

    the_key = len(array)

    cool=[]
    for j in my_interval(0,the_key-1,2):
        if j+1 <  the_key:
            b = array[j+1]
        else:
            b= []
        a = array[j]
        pair= merge(a,b)
        cool.append(pair)
    if len(cool)>1:
        return sorty(cool)
    else:
        return cool[0]
#bubble sort
def sort_bubble(array):
    """ Inline bubblesort sort.
    modifies the input array directly
    """
    # TODO (OPTIONAL): implement bubblesort sort
    # replace the lines below with your own code
    n= 0  #counter
    for j in range(0,len(array)-1,1):
    ##swaping
        if array[j ]>array[j+1]:
            swap  = array[j]
            array[j] = array[j+1]
            array[j+1]  = swap
            n += 1
    if n== 0:
        return array
    else:
        return sort_bubble(array)

def sort_selection(array):
    sorted=[]
    while len(array)> 1:

        smallest =min(array)
        array.remove(smallest)

        sorted.append(smallest)

    return sorted


print(sorty(array1))
print(my_sort(array))
print(sort_bubble(array))
print(sort_selection(array))
