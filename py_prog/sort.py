"""
# QUESTION: 1
given that an arbitrary n items array and an element due to be founded
the simple search function will at most search throughout all componets
of the array. hence the function will be executed n times


# QUESTION: 2
"""
el = int(input("give me the element to be founded:"))
n = int(input("array length is : "))
array = [ int(input("input sorted  array element :")) for i in range(n)]
def sorted_search(el,array):
    """
    define the initial length of the interval
    """
    m= 0
    count =0
    end = len(array)-1
    stop = False
    while m <= end  and not stop:
        half =(  m +end ) //2
         #the pivot point will decided whether
         # to keep spliting the interval IF SO which half will survive
         # or stop the iterations if the element to be found coincides

        if el == array[half] :
            count += 1

#element coincides
            print('when i close my eyes i see you in : '  )
            print(half +1, 'position')
            print('by the way it took me ')
            print(count)
            print('tries')
            stop = True
        else :

            if el < array[half]:
                #the element is in the left side of the pivot point

                count += 1
                #reduce the length of the interval to the left side interval
                end = half -1



            if el >array[half]:
                #the element is in the right side of the pivot point

                m = half +1
                count += 1
                #reduce the length of the interval to the right side interval
            if m == end and array[m] != el :
                #the element is missing =(
                print ('who are you')
                stop = True


sorted_search(el,array)



"""
# QUESTION 3:
every time we split the array into half we end up with N/2^i terms left to be checked
this process will eventually leave us  at most with a one element interval from which the
existence of the desired element in the array is due to be decided.henceforth , if we call
the greatest number of iterations needed to decide presence of el in array count
we find that
N/2^(count)  = 1
solving for count
count=  log_{2} (N)
"""
