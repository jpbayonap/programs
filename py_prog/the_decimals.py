import random

STRENGTH = [19, 100, 31, 63, 20, 31, 83, 31, 82, 40, 96, 81, 96, 76, 82, 37, 52, 78, 30, 94, 53, 58, 9, 85, 41, 83, 4, 47, 47, 43, 34, 26]

player1=random.randint(0,31)
player2=random.randint(0,31)

#print(PROB_STRENGTH1)
#print(PROB_STRENGTH2)



def compute_winner(player1, player2):
    """ Compute the winner between two players.
    
    This function is deterministic.
    The strongest player always wins against a weaker opponent.
    In case of tie (same strength), the first player wins.
    """
    PROB_STRENGTH1 = int(round(STRENGTH[player1]/(STRENGTH[player1]+STRENGTH[player2]),1)*10)
    PROB_STRENGTH2 = int(round(STRENGTH[player2]/(STRENGTH[player1]+STRENGTH[player2]),1)*10)   


    MATCH=[0]*PROB_STRENGTH1+[1]*PROB_STRENGTH2
   
    destiny= random.randint(1,len(MATCH))

    
  
    if MATCH[destiny-1] == 0:
        return player1 
    else:
        return player2


print(compute_winner(player1,player2))
