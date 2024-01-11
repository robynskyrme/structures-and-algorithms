# 15.5.2023
# Binary Insertion Sort

# 7.6.2023 -- Been putting this off for weeks only to find i've already done it and just have to comment it.... (!)


import math
import random
import time

def binary_search(a, val, start, end):

                            # The 'last case' recursively -- if the section being checked is of length 1,
    if start == end:
        if a[start] > val:
                            # either give the new item's position as one before it, if it's smaller
            return start
        else:
                            # or one above it, if it's larger
            return start + 1


                            # Code to catch maximum recusrion error --  ** I don't understand this, or why it happens **
    if start > end:
       return start

                            # The recursive bit! Split the array into two, and, depending on where the value falls,
                            # do that with the half, and with half of that, and so on
    mid = (start + end) // 2
    if a[mid] < val:
        return binary_search(a, val, mid + 1, end)
    elif a[mid] > val:
        return binary_search(a, val, start, mid - 1)
    else:
        return mid


def BinaryInsertionSort(a):
    for i in range(1, len(a)):
        val = a[i]
        j = binary_search(a, val, 0, i-1)
                            # Piece the array back together from the start to the search position returned +
                            # the new value, the array up to where the value was, and the array from above the value to the end
        a = a[:j] + [val] + a[j:i] + a[i + 1:]
    return a



if __name__ == "__main__":
    a = []
    for j in range(17):
        a.append(random.randint(1, 200))


    print(a)

    start = time.time()
    a = BinaryInsertionSort(a)
    elapsed = time.time()-start
    print("Sorted by bianry insertion sort in " + str(elapsed) + " seconds:")
    print(a)