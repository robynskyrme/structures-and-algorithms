# 9.5.2024
# AVL tree

# seemed to work; is now broken again. No idea what the problem is

import sys

# Create a tree node
class AVL_node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL_tree(object):

                            # FUNCTION: get_height
                            # gets height of given node
    def get_height(self, root):
                            # if root given is None then height is 0
        if not root:
            return 0
                            # if root is not None it will already have a height: return it
        return root.height


                            # FUNCTION: get_balance
                            # of the given node: returns the difference in heights between left and right children
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)


                            # FUNCTION: insert
                            # takes the root node being handled, and the key to be inserted
                            # returns a node
    def insert(self, root, key):
        print(key)

                            # if no root is given (or root = None) simply create a new node with the key and return that node
        if not root:
            return AVL_node(key)
                            # if root is given, but key is less. call insert recursively making root's empty left into node of key
        elif key < root.key:
            root.left = self.insert(root.left, key)
                            # otherwise, key is larger: call insert recursively on root's empty right making it node of key
        else:
            root.right = self.insert(root.right, key)

                            # set the height of current node (root)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

                            # check if it's balanced
        balance = self.get_balance(root)
                            # two checks which only run if it's unbalanced:
                            # (balance = left.height - right.height)
                            # first, if the left is more than 1 higher than the right:
        if balance > 1:
                            # if the key just added is less than node's left root, call rotate_right
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                            # otherwise, rotate_left
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

                            # the same, the for the other case (right more than 1 higher than left)
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

                            # FUNCTION: rotate right
    def rotate_right(self,node):
                            # the following four lines took me about eight thousand years to write
        new_root = node.left
        LR_becomes_new_RL = new_root.right
        new_root.right = node
        node.left = LR_becomes_new_RL
                            # update the heights
        node.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return new_root


                            # FUNCTION: rotate left
    def rotate_left(self,node):
                            # maybe should have done left first, this was a bit easier. Still though
        new_root = root.right
        RL_becomes_new_LR = new_root.left
        new_root.left = node
        node.right = RL_becomes_new_LR
                            # update the heights
        node.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return new_root






                            # FUNCTION: print
                            # (taken and tweaked from somewhere online til I write my own)
    def print_tree(self, node, indent, last):
        if node != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("L----")
                indent += "     "
            else:
                sys.stdout.write("R----")
                indent += "|    "
            sys.stdout.write(str(node.key))
            sys.stdout.write("\n")
            self.print_tree(node.right, indent, False)
            self.print_tree(node.left, indent, True)

if __name__ == "__main__":

    tree = AVL_tree()
    root = None
    test = [30,20,40,10,5]
    for n in test:
        root = tree.insert(root, n)

    tree.print_tree(root, "", True)



