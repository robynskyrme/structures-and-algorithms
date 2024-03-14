
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

def print_list():
    index = 0
    index = find_index_of_start()
    max = len(list)


    for count in range(max):
    #    print(index)
        parent = list[index].p
        child = list[index].c
        #print(index)
        slab = ""
        # Add its parent
        if parent != 12345:
            slab = slab + "[" + str(parent) + "] " + str(list[parent].n) + "  >>>    "
        else:
            slab = slab+("              ")
        # Add current
        slab = slab + "[" + str(index) + "]" + str(list[index].n)
        # Add its child
        if child < max:
            slab = slab + "    >>>  " + str(list[list[index].c].n) + "[" + str(child) + "] "
        index = list[index].c
        print(slab)

def larger_than_child(index):
    ans = True
    if has_child(index):
        if list[index].n < list[list[index].c].n:
            ans = False
    return ans

def is_descending_order():
    index = find_index_of_start()
    length = len(list)

    # Variable to be switched off if a single pair is n < m
    d = True

    for count in range(length-1):
        if not larger_than_child(count):
            d = False

    return d

def has_child(n):
    max = len(list)
    answer = False
    if list[n].c < max:
        answer = True
    return answer

def has_parent(n):
    print(n)
    print("parent test")
    answer = False
    if list[n].p != 12345:
        answer = True
    print(answer)
    return answer

def swap_node_with_child(n):
    parent = list[n].p
    child = list[n].c


    if has_child(n):
        list[child].p = parent
        list[n].c = list[child].c
        list[list[child].c].p = n
        list[child].c = n


    list[n].p = child

    if has_parent(n):
        list[parent].c = child



if __name__ == '__main__':

    # Create a random list of a given length
    fill_random_list(7)

    # Print the entire thing, all pointers shown
    print_list()

    if is_descending_order():
        print(".... in descending order")
    else:
        print(".... not in descending order")

    userinput = ""
    while userinput != "q":
        userinput = input("Swap which node with its child: ")
        i = int(userinput)
        swap_node_with_child(i)
        print_list()
        print("\n")


    print_list()
    print(".... in descending order")