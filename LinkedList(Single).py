# 4.4.2024
# Quick singly linked list, I felt I wanted practice in coding one from scratch without reference


                            # node class: contains only the value, and the pointer to the next node
class SLLnode:
    def __init__(self,val):
        self.val = val
        self.forward = None


                            # the list object initializes with a value, assigned to the 'head' node
class SLL:
    def __init__(self, val):
        self.head = SLLnode(val)


                            # 'add to end': scrolls through all nodes in list until it reaches the last
                            # could also be stored in a 'tail' variable but this is deliberately basic
    def addtoend(self,val):
        current = self.head
        while current.forward != None:
            current = current.forward
                            # creates a new node, and simply points the last node in the list to it
        new = SLLnode(val)
        current.forward = new

                            # 'add to start'
    def addtostart(self,val):
                            # creates a new node, simply points it to the former head and reassigns it as new head
        new = SLLnode(val)
        new.forward = self.head
        self.head = new

                            # return list as array
                            # starts with head; follows pointers and appends values one by one
    def array(self):
        arr = []
        current = self.head
        while current != None:
            arr.append(current.val)
            current = current.forward
        return arr


                            # find: sinmply returns index at which query first appears, or false if it doesn't
    def find(self,query):
        current = self.head
        index = 0
        while current != None:
            if current.val == query:
                return index
            current = current.forward
            index += 1
        return False

                            # delete item at a certain index
    def delete(self,index):
                            # special case for head
        if index == 0:
            self.head = self.head.forward
                            # deleting in the middle is easy
        current = self.head
        point = 0
        while current != None:
            if point == index-1:
                current.forward = current.forward.forward
                return
            current = current.forward
            point += 1


if __name__ == "__main__":
                            # create instance of list (initalized with head value)
    list = SLL(0)
                            # add a few items
    list.addtoend(1)
    list.addtoend(2)
                            # add at the start
    list.addtostart(5)
    list.addtostart(73)
                            # list them
    print(list.array())
                            # return index of an item that's been added
    print(list.find(1))
                            # search for an item that isn't there
    print(list.find(4))
                            # delete the head
    list.delete(0)
    print(list.array())
                            # delete arbitrary index
    list.delete(2)
    print(list.array())
                            # delete 'tail' (just to check it doesn't need a special case -- it doesn't)
    list.delete(2)
    print(list.array())