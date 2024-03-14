# 14.3.2024
# heap -- build_max_heap, max_heapify

# implicit heap, in an array structure

import random
import math

def parent(n):
    return math.floor(n/2)

def left(n):
    return n*2

def right(n):
    return n*2+1

def swap(H,x,y):
    old_x = H[x]
    H[x] = H[y]
    H[y] = old_x

def max_heapify(H,k):
                            # check its children are both smaller: if so, return it as-is
    if H[left(k)] < H[k] and H[right(k)] < H[k]:
        return

                            # if the left child is larger, swap with parent
    if H[left(k)] > H[k]:
        swap(H,left(k),k)
                            # and, if it isn't a leap, max_heapify it
        if left(k) < len(H)/2:
            max_heapify(H,left(k))

                            # if the right child is larger, swap with parent
    if H[right(k)] > H[k]:
        swap(H,right(k),k)
                            # and, if it isn't a leaf, max_heapify it
        if right(k) < len(H)/2:
            max_heapify(H,right(k))

    return



def build_max_heap(H):
                            # take 1 off n since zeroth array element is not used
    n = len(H)-1

                            # start counting down from the parent of the rightmost two leaves [n-2 and n-1]
    i = math.floor(n/2)

    while i > 0:
        max_heapify(H,i)
        i -= 1


if __name__ == "__main__":

    list = ['HEAP_ZERO_INDEX']

    for j in range(15):
        list.append(random.randint(0, 100))

    print(list)

    build_max_heap(list)

    print(list)



