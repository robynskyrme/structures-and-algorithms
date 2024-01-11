# 15.2.2023 Trying a doubly linked lis / unary heap, with a method to sort

import random

class node:

    def __init__(self, p, n, c):

        # p/n/c for parent, [value of] node, child

        self.p = p
        self.n = n
        self.c = c

list = []

    # l for length of list
def fill_random_list(l):
    for c in range(l):
        rand = random.randrange(1,999)
        list.append(node(c-1,rand,c+1))

        # This is messy. But I've marked the start and end of the list with distinctive and easily findable numbers
        # '0' didn't work because the zeroth position is a valid index: how else can I solve this?
    list[0].p = 171717
    list[len(list)-1].c = 191919

def find_index_of_start():
    k = 0
    for c in range(len(list)):
        if list[c].p == 171717:
            k = c
    return k


    # s = True to print the list simply as a string, following pointers; False to show all pointers
def print_list(s):
    index = 0
    index = find_index_of_start()

    if not s:
        print("all pointers and data")
        child = 0
        # Empty string to add information to as it reads
        slab = ""

        while child != 191919:
            # Add the parent information
            slab = slab + "[" + str(list[index].p) + "]  "
            # Add the node information
            slab = slab + str(list[index].n)
            # Add the child information
            slab = slab + "   [" + str(list[index].c) + "]\n"

            child = list[index].c
            index = index + 1

        print(slab)

    if s:
        # Empty string to add to as it reads
        slab = ""

        while index != 191919:
            # Add the node information
            slab = slab + str(list[index].n) + " "

            index = list[index].c

        return slab


def is_descending_order():
    index = find_index_of_start()

    # Variable to be switched off if a single pair is n < m
    d = True

    # I'm not happy about having to change this while loop to count the CHILD rather than the current but it fixed the problem
    while list[index].c != 191919:
        if list[index].n < list[list[index].c].n:
#            print(str(list[index].n) + " < " + str(list[list[index].c].n))
            d = False
        index = list[index].c

    return d

def sort_list():
    index = find_index_of_start()
    while list[index].c != 191919:
        if list[index].n < list[list[index].c].n:
            swap_with_child(index)

        index = list[index].c

    # Method to swap a node with its child
def swap_with_child(index):
    parent = list[index].p
    child = list[index].c

    # Set current node's parent to be its current child
    list[index].p = child
    # Set current node's child to be the child of its child
    list[index].c  = list[child].c

    # Set parent node's child to be current child
    list[parent].c = child

    # Set child's child to be current node
    list[child].c = index
    # Set child's parent to be current parent
    list[child].p = parent

    # Set child's child's parent to be current node
    list[list[child].c].p = index

# Main body

if __name__ == '__main__':

        # Create a random list of 23 items
    fill_random_list(11)

        # Print the entire thing, all pointers shown
    print_list(False)

        # Print the list as indicated by the pointers
    list_as_string = print_list((True))
    print(list_as_string)

    if is_descending_order():
        print(".... in descending order")
    else:
        print(".... not in order")


    while not is_descending_order():
        sort_list()
        list_as_string = print_list((True))
        print(list_as_string)

    print_list(False)

    list_as_string = print_list((True))
    print(list_as_string)


