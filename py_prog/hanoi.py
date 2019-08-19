## things  to do
# define disk ,peg  and source
import time
n = int(input("n = "))





def print_pegs(pegs):
    """Prints the pegs and the disks they contain."""
    for i, peg in enumerate(pegs):
        print(f"{i}: {pegs[i]}")
    for i in range(3):
        print(pegs[i])
        if len(pegs[i]) ==0 :
            print(''+'peg  feels so lonely')
        else:
            for  hola in reversed(pegs[i]):
                print(  ' '*( 2*( len(pegs[i])-hola))+'hanoi'*(hola+1))





def move_disk(pegs, disk, source, dest):
    """Moves a single disk from peg source to peg dest.

    Args:
        pegs (array):       Array holding the pegs
        disk ({0,...,n-1}): Number of the largest disk in the tower to move
        source ({0,1,2}):   Source peg (i.e., in which the tower is originally)
        dest ({0,1,2}):     Destination peg (i.e., where to put the tower)
    """
    print(f"STEP: move disk {disk} from peg {source} to peg {dest}")
    # check if the move is valid
    if source < 0 or 2 < source: raise AssertionError("source index out of bounds")
    if dest   < 0 or 2 < dest:   raise AssertionError("destination out of bounds")
    if pegs[source][-1] != disk: raise AssertionError("wrong disk in source peg")
    if pegs[dest] and (pegs[dest][-1] <= disk): raise AssertionError("destination has smaller disk")

    # do the move
    pegs[source].pop()
    pegs[dest].append(disk)

    # show the new state
    print_pegs(pegs);


def move_tower(pegs, disk, source, dest):
    """Moves a whole tower from one peg to another.

    Args:
        pegs (array):       Array holding the pegs
        disk ({0,...,n-1}): Number of the largest disk in the tower to move
        source ({0,1,2}):   Source peg (i.e., in which the tower is originally)
        dest ({0,1,2}):     Destination peg (i.e., where to put the tower)
    """
    spare = 3-source-dest
      # number of the third peg (i.e., neither source nor dest)
    # TODO: (code missing) solve the Tower of Hanoi puzzle.
    # use function move_disk(...) to move a disk from one peg to another.

    if disk == 1 :
         move_disk(pegs,disk-1,source,dest)

    else:
        move_tower(pegs,disk-1,source,spare)
        move_disk(pegs,disk-1,source,dest)
        move_tower(pegs,disk-1,spare,dest)

def hanoi(n):
    """Solves the "Tower of Hanoi" puzzle for n disks."""
    if n <= 0: raise "n must be positive"

    # Initial settings
    pegs = [[] for i in range(3)]
    pegs[0] = list(x for x in reversed(range(n)))

    # show initial state
    print("Start")
    print_pegs(pegs)



    # move the tower
    move_tower(pegs, n, 0, 1)






hanoi(n)




    #    return move_disk(pegs,n-2,0,2), move_disk(pegs,n-3,0,1) , move_disk(pegs,n-2,2,1)
