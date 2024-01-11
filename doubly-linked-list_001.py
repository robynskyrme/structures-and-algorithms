# 22.1.2023 Trying a doubly linked list

class node_double:

    def __init__(self, back, value, fwd):

        self.back = back
        self.value = value
        self.fwd = fwd

list = []

# This bed is too cold for my tired head
# Bring me a hill soft with trees
# Tuck a cloud up under my chin ...
# ( https://youtu.be/JvkGKTsFQ3Y )

list.append(node_double(0,"Lord,",2))
list.append(node_double(4,"please",1))
list.append(node_double(0,"blow",3))
list.append(node_double(2,"the",5))
list.append(node_double(5,"out",1))
list.append(node_double(3,"moon",4))

# Function to print all info about a given node

def printcurrent():
    print (str(list[current].back) + " << " + list[current].value + "[" + str(index) + "] >> " + str(list[current].fwd))


# Just print the number which keeps track of its place in the list
def printindex():
    print (index)

# Don't necessarily need this if the first and last items simply point to themselves, but, it stopped a few errors
def bounds():
    global index
    if index > len(list)-1:
        index = len(list)-1
    if index < 0:
        index = 0

# Function to move forward in the list a given number of steps
def fwd(n):
    global current
    global index
    index = index + n
    bounds()
    for s in range(n):
        current = list[current].fwd

# Function to move backward in the list a given number of steps
def back(n):
    global current
    global index
    index = index - n
    bounds()
    for s in range (n):
        current = list[current].back


if __name__ == '__main__':

# NB check understanding of relentless "referenced before assignment" error

    current = 0
    index = 0

# Some tests, explained in their print statements:

    for j in range (6):
        printcurrent()
        fwd(1)

    print ("\nand in reverse:\n ")

    for j in range (6):
         printcurrent()
         back(1)

    print ("\njump forward by 4 and then back by 1, then back by 3")

    printcurrent()
    fwd(4)
    printcurrent()
    back(1)
    printcurrent()
    back(3)
    printcurrent()

    print("\n... as a string:\n ")

    text = ""

    for j in range (6):
        text = text + list[current].value + " "
        fwd(1)

    print (text)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
