
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
    length = len(list)

    slab = ""

    for n in range(length):
        slab = slab + str(list[n].n)
        slab = slab + "\n"

    print(slab)

def print_pointers():
    length = len(list)

    slab = ""

    for n in range(length):
        slab = slab + "[" + str(list[n].p) + "]"
        slab = slab + str(list[n].n)
        slab = slab + "[" + str(list[n].c) + "]"
        slab = slab + "\n"

    print(slab)

def sort_list():
    length = len(list)
    for k in range(length):
        print(larger_than_child(k))
        if not larger_than_child(k):
            swap_with_child(k)


def swap_with_child(n):
    list[list[n].c].p = n
    list[n].p = list[n].c

def larger_than_child(index):
    ans = False
    if has_child(index):
        if list[index].n > list[list[index].c].n:
            ans = True
    return ans



def in_descending_order():
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

# def swap_node_with_child(n):




if __name__ == '__main__':

    # Create a random list
    fill_random_list(2)

    # Print the entire thing, all pointers shown
    print_list()
    print_pointers()

    if in_descending_order():
        print(".... in descending order")
    else:
        print(".... not in descending order")

    sort_list()

    print_list()
    print_pointers()
