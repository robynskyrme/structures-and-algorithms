# 21.5.2024
# Implementation(s) of a graph, and BFS / DFS on it

# GRAPH OF BRIGHTON, UK

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
    [0,4,7,10], # Hanover
    [3,4,5,9,10,11], # The Level
    [2,5,9], # Seven Dials
    [5,7,8,11], # Preston Circus
    [7], # Lewes Road
    [7,9], # Fiveways
]

def BFT(graph, start):
                            # a set to keep track of nodes which have been visited
    visited = set()
                            # a stack for storing nodes which need to be visited, initialized with the starting node
    stack = [start]
                            # anything that's in the stack is guaranteed to be visited; we can mark it as such immediately
    visited.add(start)

    nodes_order = []

                            # repeat the following process for as long as there is a stack of nodes to visit
    while stack:
                            # pop the top of the stack
        node = stack.pop(0)
                            # for each new node, output or store it:
        nodes_order.append(node)
                            # for every node adjacent to the current node,
        for adj in graph[node]:
                            # if it's been visited already, ignore it
            if adj not in visited:
                            # otherwise, add it to the stack, and mark it as visited
                stack.append(adj)
                visited.add(adj)

    return nodes_order


if __name__ == "__main__":
                            # these are traversals, not "searches", I think?
                            # didn't sleep last night + can't figure out how to tweak this into a "shortest path" algorithm
                            # -- something to discuss in meeting later!
    breadth_first = BFS(adjacency_list, 11)
    print(breadth_first)