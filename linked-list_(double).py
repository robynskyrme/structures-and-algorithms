# 21.5.2024
# A doubly-linked list from scratch, for practice
# This implementation does NOT keep track of the tail

import random

class node:
    def __init__(self,value,back,fwd):
        self.value = value
        self.back = back
        self.fwd = fwd


class DLL:
    def __init__(self,headvalue):
        self.head = node(headvalue,None,None)


    def print_as_array(self):
        output_array = []
        caret = self.head
        while caret:
            output_array.append(caret.value)
            caret = caret.fwd

        print(output_array)


    def add_to_start(self,value):
        temp_node = node(value,None,self.head)
        self.head.back = temp_node
        self.head = temp_node

    def add_to_end(self,value):
        temp_node = node(value,None,None)
        caret = self.head
        while caret.fwd:
            caret = caret.fwd
        caret.fwd = temp_node
        caret.fwd.back = caret


    def get_node(self,value):
        caret = self.head

        while caret.value is not value:
            if caret.fwd == None:
                return False
            caret = caret.fwd


        return caret


    def delete_value(self,value):
        caret = self.get_node(value)

        if caret.fwd and caret.back:
            caret.back.fwd = caret.fwd
            caret.fwd.back = caret.back

        if caret.fwd and not caret.back:
            caret.fwd.back = None
            self.head = caret.fwd

        if caret.back and not caret.fwd:
            caret.back.fwd = None


    def read_back_from_value(self,value):
        caret = self.get_node(value)

        while caret:
            print(caret.value)
            caret = caret.back

        print(" ")



if __name__ == "__main__":
    example = DLL(5)
    example.print_as_array()

    example.add_to_start(2)
    example.print_as_array()

    example.add_to_start(1)
    example.print_as_array()

    example.add_to_end(6)
    example.print_as_array()

    example.delete_value(2)
    example.print_as_array()

    example.add_to_start(0)
    example.print_as_array()

    example.read_back_from_value(6)

    example.delete_value(5)

    example.read_back_from_value(6)

    for i in range(163):
        example.add_to_end(random.randint(1,100))

    example.print_as_array()
    example.read_back_from_value(73)