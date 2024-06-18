# Very basic graph for testing Dijkstra
# Trying Dijkstra WITHOUT CLASSES to begin with
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
        node = distance.index(min((x for x in distance if x is not None), default=None))
                            #  PROBLEM HERE

                            # For each of its immediate neighbours...
        print(node)
        for neighbour_distance in range(len(neighbour[node])-1):

            if neighbour[node][neighbour_distance] and distance[node]:
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
        distance[node] = None

                            # Tripwire! If the target/end node has now been hit, just return the route to it...

    print(via)
    return get_route_home(start,end,via)

def get_distance_neighbour(start,end):
    return neighbour[start][end]

def get_route_home(start,end,via):
    rs = 19

    route = []

    node = end

    while node is not start:
        route.append(node)
        node = via[node]

    route.append(start)

    print("Route: " + str(route))



if __name__ == "__main__":
    #print(neighbour)
    #print(get_distance_neighbour(1,2))

    print(dijkstra(0,3))