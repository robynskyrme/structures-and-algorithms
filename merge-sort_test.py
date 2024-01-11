# 17.5.2023
# Merge sort
# (from scratch)

def MergeSort(a):
    if len(a) < 2:
        return a

    length = len(a)

    half = length//2

    left = a[:half]
    right = a[half:]

    left = MergeSort(left)
    right = MergeSort(right)

                            # From here on I got stuck and consulted this https://www.scaler.com/topics/merge-sort-in-python/
                            # Code outputs
                            #    [6, 3, 9, 2, 0, 4, 1] (unsorted)
                            #    [0, 3, 6, 9, 2, 1, 4] ("Sorted") so something's wrong

    # Initial values for pointers that we use to keep track of where we are in each array
    i = j = k = 0

    # Until we reach the end of either start or end, pick larger among
    # elements start and end and place them in the correct position in the sorted array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

        # When all elements are traversed in either left or right,
        # pick up the remaining elements and put in sorted array
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1


    return a



if __name__ == "__main__":


    unsorted = [6,3,9,2,0,4,1]

    print(unsorted)
    sorted = MergeSort(unsorted)
    print(sorted)