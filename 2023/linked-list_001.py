
# 21.1.2023 -- first attempt at a linked list
# And actually at a GitHub upload

# Create class for the node of a single-linked list
# (will not be attempting double yet)

class node_single:

    # each node stores itself plus a 'forward' pointer
    def __init__(self, value, fpoint):

        # I'm coping this line from a webpage and I don't really understand it
        self.value = value
        self.fpoint = fpoint

list = []


# Example list 1: The numbers 1-5, pointers such that if read correctly they are in the right order
# list.append(node_single(1,4))
# list.append(node_single(3,3))
# # This node points to an imaginary node, not on the list
# list.append(node_single(5,5))
# list.append(node_single(4,2))
# list.append(node_single(2,1))

# Example list 2: Six words, ditto
list.append(node_single("Every",3))
list.append(node_single("boy",2))
list.append(node_single("deserves",5))
list.append(node_single("good",1))
# Points outside of list
list.append(node_single("lists",6))
list.append(node_single("linked",4))



# Method to get the nth item from the list
def read_linkedlist(n):
    # Which node is being accessed
    ll_current = 0
    # Which node is being pointed to by that node
    ll_pointer = 0
    # Keep track of how many you are counting
    item = 0

    # Variable to switch off to end a while loop
    reading = True

    while reading:
        # Read the value of the node
        v = list[ll_current].value
        # Read the pointer to the next node
        ll_pointer = list[ll_current].fpoint


# Only count as far as you're told
        if item == n:
            reading = False

        # Reassign the linked node as the current one
        ll_current = ll_pointer
        # Tally
        item = item + 1

    # Give back the value of the node reached
    return v



# Method to simply list the whole thing
def list_linkedlist():
    ll_current = 0
    ll_pointer = 0
    d = ""
    reading = True
    while reading:

        ll_pointer = list[ll_current].fpoint
        v = list[ll_current].value

        # Add the current value to a string
        d = d + str(v)

        # Slightly different check -- stop when length of list is reached
        if ll_pointer == len(list):
            reading = False
        else:
        # This is cosmetic
            d = d + ", "

        # Reassign linked node as current
        ll_current = ll_pointer

    # Give the string back
    return d



    # Demonstrations
if __name__ == '__main__':

    # Print the first, and last, and third, items in the list
    print ("First: " + str(read_linkedlist(0)))
    print ("Fifth: " + str(read_linkedlist(4)))
    print ("Third: " + str(read_linkedlist(2)))

    # List the items accessed individually
    print ("Listed via a for-loop:")
    for c in range (0,len(list)):
        item = read_linkedlist(c)
        print (item)

    # Reel the whole list off in one go
    print ("Listed in a single function:")
    d = list_linkedlist()
    print (d)



