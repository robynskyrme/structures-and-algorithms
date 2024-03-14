# 29.3.2023
# Implicit heap stored as list; no pointers used
#
# Practise for sort, insert, delete etc.
#
# So far only very basic iterative heapify on every single node but I think it does work
#
# Generates random heap, then loops heapifying each node  in turn, 100 times


import random

implicit_heap = []
def random_fill(size):
    implicit_heap.append(0)
    for j in range(size):
        k = random.randint(1,19)
        implicit_heap[0] += 1
        implicit_heap.append(k)


def display_heap(heap):
                            # This isn't pretty but it KIND OF outputs the heap to give a visual sense of it
    width = 50
    index = 1
    layer = 0
    count = 0

    output = ""

    while index <= heap[0]:

        for pad in range(int(width/2**layer)):
            output = output + " "

        output = output + str(heap[index])
        cutoff = 2 ** layer-1
        index += 1
        count += 1

        if count > cutoff:
            output = output + "\n\n"
            layer = layer + 1
            count = 0

    print(output)


def heapify_node(heap,n):
    if 2*n >= heap[0]:
        leftchild = 0
        rightchild = 0
    else:
        leftchild = heap[2*n]
        rightchild = heap[2*n + 1]

    if leftchild > heap[n]:
        oldn = heap[n]
        oldleft = leftchild
        heap[n] = oldleft
        heap[2*n] = oldn

    if rightchild > heap[n]:
        oldn = heap[n]
        oldright = rightchild
        heap[n] = oldright
        heap[2*n+1] = oldn



if __name__ == "__main__":
    random_fill(18)

    print(implicit_heap)
    display_heap(implicit_heap)
    print ("\n\n\n")


                            # No recursion, just iterate over the whole list, heapifying each node
    for k in range(100):

        for j in range(implicit_heap[0]):
            heapify_node(implicit_heap,j)

    print(implicit_heap)
    display_heap(implicit_heap)