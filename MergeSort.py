# 11.3.2024
# Merge Sort

import random

def MergeSort(list):
                            # the base case: a string of length 1 is already sorted, so return it
    if len(list) == 1:
        return list

                            # create a list which the halves will be merged into
    result = []

                            # integer that splits the list in two (exactly if even, lopsided if list is odd)
    half = int(len(list)/2)

                            # recursion: both halves are themselves merge-sorted
    left = MergeSort(list[:half])
    right = MergeSort(list[half:])

                            # a count of elements, for the following while loop
    total = len(left) + len(right)
                            # while elements remain, merge the lists one element at a time
    while len(result) < total:
        if left and right:
                            # case for two elements equal (just take the left)
            if left[0] == right[0]:
                result.append(left[0])
                left = left[1:]
        if left and right:
                            # cases for two elements that differ
            if left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
                            # cases when one of the lists has been emptied
        if left and not right:
            result.append(left[0])
            left = left[1:]
        if right and not left:
            result.append(right[0])
            right = right[1:]

                            # return the merged list
    return result


if __name__ == "__main__":

                            # lots of testing
    for test in range(1000):

        list = []

        for j in range(19):
            list.append(random.randint(0,23))

        print(list)
        print(MergeSort(list))