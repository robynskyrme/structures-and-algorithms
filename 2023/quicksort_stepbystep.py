import random

mylist = [9,8,7,6,1,4,3,2,5]

def quicksort(list):
    peg = 3

    height = list[peg]

                            # Can't use forloops because the index *changes* every time an element is popped
                            # This loop finds numbers larger than the peg, appends them, and removes them
    j = 0
    while j < peg:
        print (list)
        if list[j] > height:
            print(str(list[j]) + " is bigger than " + str(height) + " so it goes to the right")
            list.append(list[j])
            list.pop(j)
            j -= 1
            peg -= 1
        j += 1

    j = peg+1
    while j < len(list)-1:
        print(list)
        if list[j] < height:
            print(str(list[j]) + " is smaller than " + str(height) + " so it goes to the left")
            list.insert(0,list[j])
            list.pop(j+1)
            j -= 1
            peg += 1
        j += 1

    print("Peg at index " + str(peg))


if __name__ == "__main__":
    quicksort(mylist)