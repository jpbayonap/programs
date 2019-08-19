"""
I use this file to generate 32 players
Then we will use the data to simulate
tournaments between these players
"""

import random
random.seed(2019)

# Number of players
NB_PLAYERS = 32

# Array (list) to store the strength of each player
players_strength = []

# Generate random strength for each player
for _ in range(NB_PLAYERS):     # _ can be used when the index is not used
    s = random.randint(0, 100)
    players_strength.append(s)

print(players_strength)

# players_strength = [19, 100, 31, 63, 20, 31, 83, 31, 82, 40, 96, 81, 96, 76, 82, 37, 52, 78, 30, 94, 53, 58, 9, 85, 41, 83, 4, 47, 47, 43, 34, 26]
