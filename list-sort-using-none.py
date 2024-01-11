# 3.3.2023
#
# Method to swap a node with its child using pointers; method to sort a list into descending order
# The actual sort method calls itself recursively and that was NOT the plan but all my other attempts failed


import random
class node:
    def __init__(self, p, v, c):

        # p/v/c for parent, value, child

        self.p = p
        self.v = v
        self.c = c

list = []


    # l for length of list; note to self: don't forget it's zero-indexed
def fill_random_list(l):
    for c in range(l):
        rand = random.randrange(1,163)
        list.append(node(c-1,rand,c+1))

    list[0].p = None
    list[l-1].c = None

    # Find the 'start' node in the list, the one with no parent (None)
def find_index_of_start():
    k = 0
    for c in range(len(list)):
        if list[c].p == None:
            k = c
    return k

def smaller_than_child(node):
    value = list[node].v
    child_value = list[list[node].c].v

    if value < child_value:
        smaller = True
    else:
        smaller = False
    return smaller


    # Check whether list is in order -- k = 0 to check for ascending; 1 for descending
def is_list_ordered(k):
    ordered = True
    node = find_index_of_start()
    for iter in range(len(list)-1):
        value = list[node].v
        child_value = list[list[node].c].v

        if k == 0:
            if not smaller_than_child(node):
                ordered = False
        if k == 1:
            if smaller_than_child(node):
                ordered = False

        node = list[node].c

    return ordered

def has_parent(node):
    has = True
    if list[node].p == None:
        has = False
    return has

def has_child(node):
    has = True
    if list[node].c == None:
        has = False
    return has

def node_start_list(node):
    start_list = False
    if find_index_of_start() == node:
        start_list = True
    return start_list

def swap_with_child(n):

    node = find_index_of_start()
    for iter in range (n):
        node = list[node].c

    child = list[node].c
    childs_child = list[list[node].c].c

    # Case for 'normal' nodes (in middle of list)
    if has_child(node):
        if has_parent(node):
            # Six pointers to change, in three pairs:
            # First pair: set the current node's child as the new child of the node's parent ...
            list[list[node].p].c = list[node].c
            # ... and set that old parent to be the new parent of the child
            list[list[node].c].p = list[node].p
            # Second pair: set the current node to be the child of its child ...
            list[list[node].c].c = node
            # ... and set the current node's parent to be its child
            list[node].p = list[node].c
            # Set the current node's child to be its child's child
            list[node].c = childs_child

    if not has_parent(node):

        # Two pairs:
        # First pair: set the current node to be the child of its child ...
        list[list[node].c].c = node
        # ... and set the current node's parent to be its child
        list[node].p = list[node].c
        # Second pair: set the current node's child to be its child's child
        list[node].c = childs_child
        # ... and set the child's child's parent to be the current node
        list[childs_child].p = node
        # AND set the child's parent to be nothing
        list[child].p = None

    if childs_child != None:

        # ... and, if there IS a child's child's, set the child's child's parent to be the current node
        list[childs_child].p = node


    # Output the list, following pointers from only node with None as parent
def print_list():

    list_one_line = ""

    node = find_index_of_start()
    for iter in range(len(list)):
        value = int(list[node].v)
        list_one_line = list_one_line + str(value) + " "
        node = list[node].c

    print(list_one_line)

    # Output the list as blocks; I just wanted to do it visually
def print_bargraph():

        bars = ""

        node = find_index_of_start()
        for iter in range(len(list)):
            value = int(list[node].v)
            for block in range(value):
                bars = bars + "█"
            bars = bars + "\n"
            node = list[node].c

        print(bars)

def print_data():
    slab = ""
    for index in range(len(list)):
        # Add the parent information
        slab = slab + "[" + str(list[index].p) + "]  "
        # Add the node information
        slab = slab + str(list[index].v).rjust(3, " ")
        # Add the child information
        slab = slab + "   [" + str(list[index].c) + "]\n"

    print(slab)



def sort_list():

    node = find_index_of_start()

    swap = None

    for count in range(len(list)-1):
        if smaller_than_child(node) == True:
            swap = count
        node = list[node].c

    if swap != None:
        swap_with_child(swap)
        sort_list()





    # Main body

if __name__ == '__main__':

    # Create a random list
    fill_random_list(23)

    print_data()
    print_bargraph()
    print_list()

    print("List in order:")
    print(is_list_ordered(1))

    print("\nSorting:")
    sort_list()

    print_data()
    print_bargraph()
    print_list()

    print("List in order:")
    print(is_list_ordered(1))

