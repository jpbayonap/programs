import random  # Module needed to generate "random" numbers

random.seed(123)

def one_dice(nb_simulations):
    counter = [0,0,0,0,0,0]  # shorter version is: counter = [0]*6

    for i in range(nb_simulations):
        # Throw a dice and get a random (uniform) result
        x = random.randint(1,6)
        # Be careful x is in {1,...,6}
        # but array are indexed from 0
        counter[x-1] += 1
    
    print("Raw values:", counter)
    
    for i in range(6):
        # Compute percentage and round with 2 digits after the decimal point
        counter[i] = round( counter[i] * 100 / nb_simulations, 2)    
    print("Percentage values:", counter)

# Run the simulation
one_dice(10000)

