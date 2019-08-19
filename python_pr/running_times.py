import cProfile

first=int(input("how large bro?")) #o(1)
second= int(input("what about the second"))
seq= [i for i in range(first)] #linear o(n+1)
seq_2= [i for i in range(second)]
loop =[(i+1)*[j for j in range(second)] for i in range(first)]

print (seq)
print (seq_2)
print (loop)



"""complexity for nested loops
multiply

for code blocks = same indentation
addition

"""
# o(n)*o(n) =o(n^2)
"""sum of all combinations of pairs
from a sequence  ....how to not add twice??  what about a m*m matrix """
def cuadratica(seq):
    t=0
    for j in seq: # o(n)
        for k in seq: #o(n)
            t += j*k
    return  t

"""now mix sequential and nested together """




def mix(seq):
    s=0
    for j in seq:   #entire block  o(n)*o(n+n^2) = o(n^2 +n^3)
        # inside loop o(n)+o(n^2)
        for k in seq:  #o(n)
            s += j*k
        for l in   seq: #o(n^2)
            for m in seq:
                s  += j-m
    return s
""" my attempt for not overlapping"""
def cuadratica_resta(seq):
    t=0
    count= 0
    for j in seq : #working with  elements
        count += 1
        for k in seq :
            t += j*k
        for l in range(count):
            t -= j*seq[l]
    return t


"""book cool solution
hard to find the complexity

"""

def cuadratica_book(seq):
    s= 0
    for i in range(first -1): #working with numbers

        for j in range(i+1,first):
            s+= seq[i]*seq[j]
    return s



""" things get fiddly for pseudo  matrix dudes"""

def pseudo_mix(seq, seq_2):
    a = 0
    """o(pseudo_mix) o(first)* o(second) """
    for b in seq: #o(first)
        for c in seq_2: #o(second)
            a += b*c
    return a

""" sum the iteration counts of the inner loop"""

def inner_loop(loop):
    s= 0
    for loop_2 in loop:
        for x in loop_2:
            s += x
    return s


""" input vs efficiency  cases
Best case : optimally suited input vs algorithm
worst case : worst possible running time
average : random input with given probability
"""


print(cuadratica(seq))
print(cuadratica_resta(seq))
print(cuadratica_book(seq))
cProfile.run(cuadratica(seq))
