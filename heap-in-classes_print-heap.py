# 29.3.2023
# Heap using classes and nodes and a method to display the heap
#
# Stuck. Going to abandon it for a while and rethink / start again

import random

class heap:

    def __init__(self):
            output = output =
        self = []

    def append_value(self,value):
        pass

class node:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

my_heap = heap()

# def fill_random_heap(heap,values):
#
#     index = 1
#     layer = 0
#
#     heap.append(0)
#
#     while heap[0] < values:
#         k = random.randint(1,73)
#         heap.append(node(k,index * 2,index * 2 + 1))
#         index += 1
#         heap[0] += 1


def print_heap(heap):
    for j in range(1,heap[0]):
        print(str(heap[j].value) + "    " +str(heap[j].left) + ", " + str(heap[j].right))


if __name__ == "__main__":
    #fill_random_heap(my_heap,11)

    print_heap(my_heap)

    for j in range(1,my_heap[0]):
        my_heap.max_heapify(j)

    print(my_heap)