# I'm going this week to make a new Git subdirectory of sort algorithms and keep them all in a similar "style"
# with consistent variable names (and so on)
#
# but for now -- this Heap sort is just copied over from another file. To be updated / tidied later:


import random

def max_heapify(a, size, i):
    leftchild = 2 * i
    rightchild = 2 * i + 1

    max = i

    if leftchild < size and a[leftchild] > a[i]:
        max = leftchild

    if rightchild < size and a[rightchild] > a[max]:
        max = rightchild

    if max != i:
        a[i], a[max] = a[max], a[i]
        max_heapify(a, size, max)

def build_max_heap(a):
    size = len(a)

    for i in range (size//2, 0, -1):
        max_heapify(a, size, i)

def display_heap(heap):
    # This isn't pretty but it KIND OF outputs the heap to give a visual sense of it

    width = 60
    index = 1
    layer = 0
    count = 0

    output = ""

    while index <= len(heap)-1:

        for pad in range(int(width / 2 ** (layer)+1)):
            output = output + " "

        output = output + str(heap[index])
        cutoff = 2 ** layer - 1
        index += 1
        count += 1

        if count > cutoff:
            output = output + "\n\n"
            layer = layer + 1
            count = 0

    return output


def heapsort(a):
                            # Assume it is already a heap
                            # Variable for size of heap, which will decrease
    size = len(a)-1

    sorted_list = []

                            # Repeat process for every index in heap
    for j in range(size,0,-1):
                            # Add the node at the top of the (max) heap to the new list
        sorted_list.append(a[1])
                            # Swap that node with the last leaf
        a[1], a[j] = a[j], a[1]
                            # Remove the last leaf (now the largest value)
        del a[-1]
                            # The peak of the "heap" is now a small value.
                            # Recursively heapify that until it goes where it belongs
                            # ... leaving, at the top, the new max value
        max_heapify(a, j, 1)
                            # Repeat this for every node in the heap

                            # Then return the final array, in sorted order
    return sorted_list


if __name__ == "__main__":
    a = [None]
    for j in range(73):
        a.append(random.randint(1,200))

    print(a)
    print(display_heap(a))
    print("\n\n")

    build_max_heap(a)

    print(a)
    print(display_heap(a))

    print("Sorted list: ")
    print(heapsort(a))
