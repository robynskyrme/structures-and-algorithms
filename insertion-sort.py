# 15.5.2023
# Insertion Sort

# 16.5.2023
# Insertion Sort but rewritten -- previous was really just bubble sort in reverse (swapping still happened indivudually)
# Re-coding now to preserve this distinction:
# -- bubble sort the new item moves one swap by swap til it arrives in place
# -- insertion sort, the correct place is found FIRST and the new item placed there subsequently

import math
import random
import time


                            # Method to create empty point in array a at index i
                            # (assume zero index)
def free_up_index(a,i):
    if i >= len(a):
        a.append([])
        return a

    if a[i] == []:
        return a

    a.append([])
                            # Honestly: the extra -2 and -1 surprised me, but it works!
    for j in range(len(a)-2,i-1,-1):
        a[j], a[j+1] = a[j+1], a[j]

    return a



                            # Still doesn't work, I have rewritten this about 20 times and it still doesn't even slightly work
def InsertionSort(a):
    length = len(a)

    sorted = []
    sorted.append(a[0])
    del a[0]

    for i in range(len(a)):
        pos = 0
        for j in reversed(range(len(sorted))):
            if sorted[j] < a[i]:
                pos = j

        sorted = free_up_index(sorted,pos)
        print(sorted) # hdfkg
        sorted[pos] = a[i]
        print(sorted)

    return sorted



if __name__ == "__main__":
    a = []
    for j in range(11):
        a.append(random.randint(1, 200))

    print(a)

    start = time.time()
    a = InsertionSort(a)
    elapsed = time.time()-start
    print("Sorted by insertion sort in " + str(elapsed) + " seconds:")
    print(a)