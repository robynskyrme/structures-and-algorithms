# 17.5.2023
# Merge sort
# (from scratch) (again)

# Ok it works: but I am going to debug it (!) until I understand *how* it works, because I don't have a good intuitive sense yet

def MergeSort(a):
    if len(a) > 1:
        halfway = len(a) // 2
        left = a[:halfway]
        right = a[halfway:]

                            # Recursive call on each half
        MergeSort(left)
        MergeSort(right)

                            # Variables to scroll through
        i = 0
        j = 0

                            # Iterator for the list which was passed, and which will be returned (sorted)
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:

                a[k] = left[i]

                i += 1
            else:
                a[k] = right[j]
                j += 1

            k += 1

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