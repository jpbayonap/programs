# This file can be used to run simulations and generate data
# You need to choose "good" parameters and explain your choices
# I give two examples

from simulations import variable_proba_propagation, variable_burning_duration

def cool_range(start, stop,step):
    j= start
    while j <= stop :
        yield j
        j += step


# Example of usage of variable_proba_propagation:

for j in cool_range(50,100,50):
    print("grid size")
    print(j )
    for i in cool_range(5,7,2):
        print("burning duration")
        print(i)
        variable_proba_propagation(1000, j, i, list(x/10 for x in cool_range(0,10,1)), 10000, False)
# May take 1-2min to complete with these parameters
# list(x/10 for x in range(11)) creates the list [0, 0.1, 0.2, ..., 1.0]

# Example of usage of variable_burning_duration:
for j in cool_range(50,100,50):
    print("grid size")
    print(j )
    for i in cool_range (0.4,0.5,0.1):
        print("probability")
        print(i)
        variable_burning_duration(1000, j, list(x for x in cool_range(0,14,2)), i, 10000, False)
# May take 1-2min to complete with these parameters
