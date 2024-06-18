# Very basic graph for testing Dijkstra
# Trying Dijkstra WITHOUT CLASSES, for this code


import sys

neighbour = [
    [None,1,7,7], # 0 Aberdeen
    [1,None,None,1], # 1 Brighton
    [7,None,None,7], # 2 Cardiff
    [7,1,7,None] # 3 Dundee
]

def dijkstra(start,end):
    if start == end:
        return None

    visited = []
    distance = []
    via = []

    for count_nodes in range(len(neighbour)):
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
                            # While there remains an unvisited node,keep Dijkstraing
    while False in visited:
                            # node variable: current node
        node = None
                            # Set current node to the smallest distance
        print(distance)
        min = sys.maxsize
        for i in range(len(distance)):
            if distance[i] < min and visited[i] == False:
                min = distance[i]


                            # THIS IS WERE THE PROBLEM IS
        node = distance.index(min)


                            # For each of its immediate neighbours...
        for neighbour_distance in range(len(neighbour[node])):

            if neighbour[node][neighbour_distance] is not None and distance[node] is not None:
                leg = distance[node] + neighbour[node][neighbour_distance]

                            # if the distance to the neighbour VIA NODE (next leg) is less than stored node distance
                if distance[neighbour_distance] and leg < distance[neighbour_distance]:
                    print("trip")
                    distance[neighbour_distance] = leg
                    via[neighbour_distance] = node

        '''print("fox")
        print(distance)
        print(via)'''


#        distance[3] = 2

        visited[node] = True

        print(visited)
                            # Tripwire! If the target/end node has now been hit, just return the route to it...
        if visited[end]:
            return get_route_home(start, end, via)

    return get_route_home(start, end, via)

def get_distance_neighbour(start,end):
    return neighbour[start][end]

def get_route_home(start,end,via):
    rs = 19

    route = []

    node = end

    while node is not start:
        route.insert(0,node)
        node = via[node]

    route.insert(0,start)

    print("Route: " + str(route))



if __name__ == "__main__":
    #print(neighbour)
    #print(get_distance_neighbour(1,2))

    print(dijkstra(0,3))