
n = int(input("n "))
# initial conditions
hell = [[] for i in range(3)]

hell[0]= list(x for x in reversed (range(n)))

def animation(hell):

    for i in range(3):
        print(hell[i])
        if len(hell[i]) ==0 :
            print(''+'peg  feels so lonely')
        else:
            for  hola in reversed(hell[i]):  #try without reversed
                print(  ' '*( 2*( len(hell[i])-hola))+'hanoi'*(hola+1))


def move_it(hell,source,dest,disk):
    hell[source].pop()
    hell[dest].append(disk)
    print(hell)


for i in range(n):
    move_it(hell,0,1,i)
    animation(hell)
