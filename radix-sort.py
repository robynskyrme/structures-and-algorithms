# 13.5.2023
# Radix Sort (LSD)
# No problems at all here! Worked first time! What an incredibly rare treat lol



import math
import random
import time

                            # Method to fish out an individual digit of a number
                            # n is a number, c is the column as a power of ten
def digit(n,c):
                            # by a happy accident (for radix) this returns '0'
                            # for empty place values rater than throwing an error,
                            # so that deals with the "pad with leading zeroes" aspect in advance

                            # remove higher place-values using modulo 10^column
    d = n % 10**(c+1)
                            # remove lower place values by dividing and rounding
    d = int(d/10**c)

    return d

                            # Had to look this up online, how to make a nested list into a 1-d list
def flatten(list):
    result = []
    for sublist in list:
        for item in sublist:
            result.append(item)
    return(result)


                            # Here it is
def RadixSort(a):
    sorted_list = []
                            # Get the length in digits of largest number in the list
    digits = int(math.log10(max(a))+1)

                            # Create some variables
    silos = []



                            # For each place value,
    for d in range(digits):
                            # For a start, maketen new silos -- one for each digit in the radix base 10
        silos = []
        for j in range(10):
            silos.append([])

                            # For every item in the list, however far it's sorted, simply
                            # assign it a silo based on the digit (d) currently being looked at
        for n in a:
            silos[digit(n,d)].append(n)

                            # Replace the original list with sorting progress so far
        a = flatten(silos)
                            # Loop til all digits done

                            # Make the nested result one-dimensional, and return it
    sorted_list = flatten(silos)

    return sorted_list




if __name__ == "__main__":
    a = []
    for j in range(73):
        a.append(random.randint(1, 200))


    print(a)

    start = time.time()
    a = RadixSort(a)
    elapsed = time.time()-start
    print("Sorted by radix sort in " + str(elapsed) + " seconds:")
    print(a)