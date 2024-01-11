# Bubble Sort

import random

def BubbleSort(a):

    n = len(a)
                           # Variable for minor optimization **
    swapped = False

                           # Cycle through subsets of elements (1, 1-2, 1-3 ... 1-n)
    for j in range(n-1):

                           # For each subset, look at each individual element ....
        for k in range(n-j-1):
                           # ... compare with its successor, and swap if necessary
            if a[k] > a[k+1]:
                swapped = True
                a[k], a[k+1] = a[k+1], a[k]

                            # ** Optimization I found online: if not one swap is needed
                            # then things are already in place so the main loop can be exited
        if not swapped:
            return




if __name__ == "__main__":
    a = []
    for j in range(73):
        a.append(random.randint(1,200))

    print(a)
    BubbleSort(a)
    print("Sorted list:")
    print(a)