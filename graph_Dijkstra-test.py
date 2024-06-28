
# Dijkstra's algorithm -- without classes, to begin with

# 19.6.2024 Works on basic graph of ABCD square with AD vertices also connected
# Tested for various start/end nodes and with various weighting combinations

# 19.6.2024 Works on more complex graph of Brighton (see below)

''' graph = [
    [None,1,7,7], # 0 Aberdeen
    [1,None,None,5], # 1 Brighton
    [7,None,None,7], # 2 Cardiff
    [7,5,7,None] # 3 Dundee
] '''


# Test graph of BRIGHTON, UK as a walking map
# Weightings are how steep/arduous the hill is

graph = [
    [None, None, None, None, 2, None, 7, None, None, None, None, None], # 0 Kemp Town
    [None, None, 2, None, 1, 2, None, None, None, None, None, None], # 1 The Lanes
    [None, 2, None, 0, None, None, None, None, 5, None, None, None], # 2 Churchill Square
    [None, None, 0, None, None, None, None, None, None, None, None, None], # 3 Palmeira Square
    [2, 1, None, None, None, 2, 8, 0, None, None, None, None], # 4 Old Steine
    [None, 2, None, None, 2, None, None, 2, 6, 1, None, None], # 5 North Laine
    [7, None, None, None, 8, None, None, 9, None, None, 6, None], # 6 Hanover
    [None, None, None, None, 0, 2, 9, None, None, 4, 0, 7], # 7 The Level
    [None, None, 5, None, None, 6, None, None, None, 8, None, None], # 8 Seven Dials
    [None, None, None, None, None, 1, None, 7, 8, None, None, 6], # 9 Preston Circus
    [None, None, None, None, None, None, 6, 0, None, None, None, None], # 10 Lewes Road
    [None, None, None, None, None, None, None, 7, None, 6, None, None] # 11 Fiveways
]

names = ["Kemp Town","The Lanes","Churchill Square","Palmeira Square","Old Steine",
             "North Laine", "Hanover","The Level","Seven Dials","Preston Circus",
             "Lewes Road","Fiveways"]




import sys

def dijkstra(start,end):
    if start == end:
        return None

    visited = []
    distance = []
    via = []

    for count_nodes in range(len(graph)):
        visited.append(False)
        distance.append(sys.maxsize)
        via.append(start)

    '''
    print(visited)
    print(distance)
    print(via)
    '''

    j = 0

    distance[start] = 0
#    print(distance)
    node = None
                            # While there remains an unvisited node, keep going
    while False in visited:
                            # Set current node to the smallest distance
        min = sys.maxsize

        for i in range(len(distance)):
            if distance[i] < min and visited[i] is False:
                min = distance[i]
                node = i


#        print("Current node is " + str(node) + ". MIN node is " + str(min))


        #print(node)

                            # For each of its immediate neighbours...
        for adj in range(len(graph[node])):

            if graph[node][adj] is not None and visited[adj] is False:
                leg = distance[node] + graph[node][adj]
                #print("Distance from " + str(start) + " to " + str(adj) + " via " +str(node) + " is " + str(leg))

                            # if the distance to the neighbour VIA NODE (next leg) is less than stored node distance
                if distance[adj] and leg < distance[adj]:
                    distance[adj] = leg
                    via[adj] = node

#            print(distance)

        '''print("fox")
        print(distance)
        print(via)'''


#        distance[3] = 2

        visited[node] = True

#        print(visited)
                            # Tripwire! If the target/end node has now been hit, just return the route to it...
        if visited[end]:
            return get_route_home(start, end, via)

    return get_route_home(start, end, via)


def get_route_home(start,end,via):

    route = []

    node = end

    while node is not start:
        route.insert(0,node)
        node = via[node]

    route.insert(0,start)

    if names:
        for node in range(len(route)):
            route[node] = names[route[node]]

    return("Route: " + str(route))


if __name__ == "__main__":

    print(dijkstra(0,10))