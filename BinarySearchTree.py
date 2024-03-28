# 28.3.2024
# Binary Search Tree

# code entered line by line from https://blog.boot.dev/computer-science/binary-search-tree-in-python/
# with own comments added, to understand and track every step

# interesting, this -- commenting on the code, as I typed it from the website, I understood it
# --- and it didn't work

# after a long time figuring out that in one of their blocks of code, some lines were  in a slightly different position,
# I confess I now *do not* quite follow how it works. The problem is with the DELETE function, in which these lines:
#
# if self.right == None:
#     return self.left
# if self.left == None:
#     return self.right
#
# initially came AFTER the two following if statements. I understood it being there... but it broke the code!
# Now that this block comes first, I cannot figure it out.


class BSTNode:
    def __init__(self,val=None):
        self.left = None
        self.right = None
        self.val = val


                                            # INSERT
    def insert(self,val):
                            # if insert called on an empty node, just assign the value
        if not self.val:
            self.val = val
            return

                            # if the node already is that value, count that as done
        if self.val == val:
            return

                            # if there is a left child, call insert recursively until reaching node without a left child
        if val < self.val:
            if self.left:
                            # and assign the value there
                self.left.insert(val)
                return
                            # if there is not a left child, make one, with the value given
            self.left = BSTNode(val)
            return

                            # no 'greater than' check as this is the only remaining option: right (= left, inverted)
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


                                            # GET MIN / GET MAX
    def get_min(self):
                            # simply zoom down the left branch until there is no longer a left child to visit
        current = self
        while current.left is not None:
            current = current.left
        return current.val

                            # max is the same, inverted for the right
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val


                                            # DELETE
                            # returns self after delete operation

    def delete(self,val):
                            # in case of nothing to delete
        if self == None:
            return self

                            # if either node is empty, simply return the other
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
                            # if the value to be deleted is less than current node, call recursively to left
        if val < self.val:
            self.left = self.left.delete(val)
            return self
                            # likewise inverted on the right
        if val > self.val:
            self.right = self.right.delete(val)
            return self
                            # these lines run if a node has two children:
                            # search for the min of the right node
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
                            # having found that, set the current node's value to that value
        self.val = min_larger_node.val
                            # and now call delete recursively on the right cihld to delete the value we have just copied
        self.right = self.right.delete(min_larger_node.val)
                            # return the current node, in its new state
        return self

                                            # EXISTS (check if a value exists)
    def exists(self,val):
                            # if the value IS the current node, excellent, True
        if self.val == val:
            return True
                            # if the value is less than the current node...
        if val < self.val:
                            # if current node has no left, then the value clearly doesn't exist
            if self.left == None:
                return False
                            # if there IS a left node, call EXISTS recursively until either it hits a TRUE or no more lefts
            return self.left.exists(val)

                            # Without a greater-than check, since these lines only run if val IS greater than self.val
                            # same as left, but inverted
        if self.right == None:
            return False
        return self.right.exists(val)

                                            # INORDER -- print the values out in order! useful
                                            # it's recursive
    def inorder(self, vals):
                            # if there's a left, go to it, call inorder recursively
        if self.left is not None:
            self.left.inorder(vals)
                            # if there isn't a left, we've reached the next value, so, append it
        if self.val is not None:
            vals.append(self.val)
                            # if there is a right child, call recursively
        if self.right is not None:
            self.right.inorder(vals)
                            # return what hsa been gathered from current node (and beneath)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals



if __name__ == "__main__":
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

    nums = [2, 6, 20]
    print("deleting " + str(nums))
    for num in nums:
        bst.delete(num)
    print("#")

    print("4 exists:")
    print(bst.exists(4))
    print("2 exists:")
    print(bst.exists(2))
    print("12 exists:")
    print(bst.exists(12))
    print("18 exists:")
    print(bst.exists(18))