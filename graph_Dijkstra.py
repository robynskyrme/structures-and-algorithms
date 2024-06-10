# Dijkstra's algorithm
# Graph of BRIGHTON, UK with weights for steepness of roads

import sys

# as an adjacency list: weighting is stored as second of tuple
graph = [
    [(4,2),(6,7)], # 0 Kemp Town
    [(2,2),(4,1),(5,2)], # 1 The Lanes
    [(1,2),(3,0),(8,5)], # 2 Churchill Square
    [(2,0)], # 3 Palmeira Square
    [(0,2),(1,1),(5,2),(6,8)], # 4 Old Steine
    [(1,2),(4,2),(7,2),(8,6),(9,1)], # 5 North Laine
    [(0,7),(4,8),(7,9),(10,6)], # 6 Hanover
    [(4,0),(5,2),(9,4),(10,0),(11,7)], # 7 The Level
    [(2,5),(5,6),(9,8)], # 8 Seven Dials
    [(5,1),(7,4),(8,8),(11,6)], # 9 Preston Circus
    [(6,6),(7,0)], # 10 Lewes Road
    [(7,7),(9,6)], # 11 Fiveways
]

def dijkstra(start,end):
                            # create a list of visited nodes (initially all False)
                            # and a list of the distance to each note, initial;y set to "infinity"
    visited = []
    distance = []
    for i in range(len(graph)):
        visited.append(False)
        distance.append(sys.maxsize)

    node = start
    distance[node] = 0
                            # get a list of neighbours (+ weights) of the node
                            # loop this, while there remain unvisited nodes
    while False in visited: # adjust later to "while False in visited"
        neighbours = get_neighbours(node)
        print(neighbours)
        for nb in neighbours:
            print(distance[node])
            print(nb[1])
                            # update node's neighbours
            if distance[node] + nb[1] < distance[nb[0]]:
                distance[nb[0]] = distance[node] + nb[1]

        visited[node] = True
        node = min(distance)



    print(distance)
    print(visited)

def get_neighbours(node):
    neighbours = []
    for i in range(len(graph[node])):
        neighbours.append(graph[node][i])

    return neighbours

if __name__ == "__main__":
    print(dijkstra(10,8))