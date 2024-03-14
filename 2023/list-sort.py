
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

    list[0].p = 12345

def find_index_of_start():
    k = 0
    for c in range(len(list)):
        if list[c].p == 12345:
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

        while child <= len(list)-1:
            # Add the parent information
            slab = slab + "[" + str(list[index].p) + "]  "
            # Add the node information
            slab = slab + str(list[index].n).rjust(3," ")
            # Add the child information
            slab = slab + "   [" + str(list[index].c) + "]\n"

            child = list[index].c
            index = index + 1

        print(slab)

    if s:
        # Empty string to add to as it reads
        slab = ""

        while index < len(list):
            # Add the node information
            slab = slab + str(list[index].n) + " "

            index = list[index].c

        return slab


def is_descending_order():
    index = find_index_of_start()

    # Variable to be switched off if a single pair is n < m
    d = True

    while list[index].c < len(list)-1:
        if list[index].n < list[list[index].c].n:
            d = False
        index = list[index].c

    return d

def sort_list():
    index = find_index_of_start()
    while list[index].c < len(list)-1:
        if list[index].n < list[list[index].c].n:
        #    print(str(list[index].n) + " is smaller than its child, " + str(list[list[index].c].n))
            swap_with_child(index)

        index = list[index].c


    # Method to swap a node with its child
def swap_with_child(index):
    print("Swapping " + str(list[index].n) + " with " + str(list[list[index].c].n))
    print(print_list(False))
    newchild = list[list[index].c].c
    # Set child's child to be current element
    list[list[index].c].c = index
    # Set parent's child to be child
    list[list[index].p].c = list[index].c
    # Set current element's child to be its child's child
    list[index].c = newchild

    if list[index].p == 12345:
        list[list[index[c].p]] = 12345



# Main body

if __name__ == '__main__':

        # Create a random list
    fill_random_list(5)

        # Print the entire thing, all pointers shown
    print_list(False)

        # Print the list as indicated by the pointers
    list_as_string = print_list((True))
    print(list_as_string)

    if is_descending_order():
        print(".... in descending order")
    else:
        print(".... not in descending order")


    scount = 0
    while not is_descending_order():
        sort_list()
        list_as_string = print_list((True))
        print(list_as_string)
        print_list(False)
        scount = scount + 1
        print(scount)
