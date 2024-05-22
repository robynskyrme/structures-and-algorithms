# 21.5.2024
# Implenetation(s) of a graph

# GRAPH OF BRIGHTON, UK stored in several different ways

                            # as an adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, "Kemp Town"],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, "The Lanes"],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, "Churchill Square"],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Palmeira Square"],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, "Old Steine"],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, "North Laine"],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, "Hanover"],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, "The Level"],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, "Seven Dials"],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, "Preston Circus"],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, "Lewes Road"],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, "Fiveways"]
]

                            # as an adjacency list
adjacency_list = [
    [4,6], # Kemp Town
    [2,4,5], # The Lanes
    [1,3,8], # Churchill Square
    [2], # Palmeira Square
    [0,1,5,6], # Old Steine
    [1,4,7,8,9], # North Laine
    [0,4,7], # Hanover
    [3,4,5,9,10,11], # The Level
    [2,5,9], # Seven Dials
    [5,7,8,11], # Preston Circus
    [7], # Lewes Road
    [7,9], # Fiveways
]

