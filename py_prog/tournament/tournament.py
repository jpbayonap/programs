"""
We would like to organize a tournament between all players.
Tournament is single-elimination bracket with a third place playoff (for the losers of semi-finals).
After the tournament, there are four players ranked 1st, 2nd, 3rd, and 4th.

Initial position in the bracket is (uniformly) random.
We want to to estimate the chance of each player to finish in a good position (1 to 4)
"""

import random

# Global variables
NB_PLAYERS = 32
STRENGTH = [19, 100, 31, 63, 20, 31, 83, 31, 82, 40, 96, 81, 96, 76, 82, 37, 52, 78, 30, 94, 53, 58, 9, 85, 41, 83, 4, 47, 47, 43, 34, 26]



def compute_winner(player1, player2):
    """ Compute the winner between two players.
    
    This function is deterministic.
    The strongest player always wins against a weaker opponent.
    In case of tie (same strength), the first player wins.
    """
    """define the probability of wining as an integer between 0 to 100"""
    PROB_STRENGTH1 = int(round(STRENGTH[player1]/(STRENGTH[player1]+STRENGTH[player2]),2)*100)
    PROB_STRENGTH2 = int(round(STRENGTH[player2]/(STRENGTH[player1]+STRENGTH[player2]),2)*100)   
    """ identify each probabilty of the players by 1  and 0 """

    MATCH=[0]*PROB_STRENGTH1+[1]*PROB_STRENGTH2
    """create an array with as many zeros or ones as their probabilities dictate """
    destiny= random.randint(1,len(MATCH))  # select a random coordinate of the MATCH vector 
  
    if MATCH[destiny-1] == 0: #decide the winer 
        return player1
    else:
        return player2


def simulate_tournament():
    """ Simulate a tournament with all NB_PLAYERS players
    
    1) Generate a random bracket
    2) Simulate the competition
    3) Return the identities of the players ranked 1 to 4
    
    Note: This function works only when NB_PLAYERS is a power of 2.
    """    
    players = list(range(NB_PLAYERS))  # List containing all players =[0,1,...,31]
    random.shuffle(players)            # Shuffle to generate random bracket

    nb_players = NB_PLAYERS  # Number of players not yet eliminated
    
    # This loop simulates all games of a given round until semi-final (excluded)
    while nb_players > 4: # Not yet semi-final
        nb_players = nb_players//2
        next_round_players = []  # List that will contain all winners of this round, i.e. players of the next round
        for k in range(nb_players):   # Given N players at the begining of the round,
            p1 = players[2*k]         # there are N//2 games to be played
            p2 = players[2*k+1]       # players[0]-vs-players[1], players[2]-vs-players[3], ...
            win_p1_vs_p2 = compute_winner(p1, p2)
            next_round_players.append(win_p1_vs_p2)
        players = next_round_players
    
    # Now there are only 4 players
    # first semi-final
    p1 = players[0]
    p2 = players[1]
    win_first_semi = compute_winner(p1, p2)
    loose_first_semi = p1 + p2 - win_first_semi     # A "nice" hack to obtain the loser player
    
    # second semi-final
    p1 = players[2]
    p2 = players[3]
    win_second_semi = compute_winner(p1, p2)
    loose_second_semi = p1 + p2 - win_second_semi
    
    # final
    rank_1 = compute_winner(win_first_semi, win_second_semi)
    rank_2 = win_first_semi + win_second_semi - rank_1
    
    # third-place game
    rank_3 = compute_winner(loose_first_semi, loose_second_semi)
    rank_4 = loose_first_semi + loose_second_semi - rank_3
    
    # Return the result of the simulation
    return (rank_1, rank_2, rank_3, rank_4)   # parenthesis are optional here


#for _ in range(10):
#    result = simulate_tournament()
#    print("Simulation result:")
#    for r, k in enumerate(result):
#        print(f"Rank {r+1}: player {k} with strength {STRENGTH[k]}")



def compute_stats(nb_simu):
    """ Compute statistics based on nb_simu tournaments """
    nb_times_in_top4 = [0]*NB_PLAYERS
    nb_times_win = [0]*NB_PLAYERS
    weakest_in_top4 = 100
    
    for _ in range(nb_simu):
        result = simulate_tournament()
        for p in result:
            nb_times_in_top4[p] += 1
            if STRENGTH[p] < weakest_in_top4:
                weakest_in_top4 = STRENGTH[p]
        for s, t in enumerate(result):
            if s ==0:
                nb_times_win[t] +=1
            else :
                nb_times_win[t] +=0

    
    percentage_in_top4 = [round(x/nb_simu*100,2) for x in nb_times_in_top4]
    percentage_win = [round(x/nb_simu*100,2) for x in nb_times_win]
    
    # data is a *bad* name. But I did not find a good name yet...
    # Create a list of pair. Each pair contains two elements:
    #     - the %age of time a player appears in top4
    #     - the identity of the player
    # Note that the order of elements (in the pair) is important for sorting
    data = [(percentage_in_top4[i], i) for i in range(NB_PLAYERS)]
    data2 =[(percentage_win[i],i) for i in range(NB_PLAYERS)]
    data.sort(reverse=True)
    data2.sort(reverse=True)
    for pair in data:
        print(f"Player {pair[1]} with strength {STRENGTH[pair[1]]} appears {pair[0]}% times in the top 4")
    for pair in data2:
        print(f"Player {pair[1]} with strength {STRENGTH[pair[1]]} appears {pair[0]}% times wined")
    
compute_stats(10000)


