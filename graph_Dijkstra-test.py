# Very basic graph for testing Dijkstra
# Trying Dijkstra WITHOUT CLASSES

# Works on basic graph of ABCD square with AD vertices also connected
# Tested for various start/end nodes and with various weighting combinations

import sys

graph = [
    [None,1,7,7], # 0 Aberdeen
    [1,None,None,5], # 1 Brighton
    [7,None,None,7], # 2 Cardiff
    [7,5,7,None] # 3 Dundee
]

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
    print(distance)
    node = None
                            # While there remains an unvisited node,keep Dijkstraing
    while False in visited:
                            # Set current node to the smallest istance
        print(distance)

        min = sys.maxsize

        for i in range(len(distance)):
            if distance[i] < min and visited[i] is False:
                min = distance[i]
                node = i


        print("Current node is " + str(node) + ". MIN node is " + str(min))


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

            print(distance)

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