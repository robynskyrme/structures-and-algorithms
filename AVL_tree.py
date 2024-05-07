# 7.5.2024
# AVL tree

class AVL_node:
    def __init__(self,val=None):
        self.left = None
        self.right = None
        self.val = val
        self.left_height = -1
        self.right_height = -1
        self.diff = 0


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
                self.left_height += 1
                self.left.insert(val)
                return
                            # if there is not a left child, make one, with the value given
            self.left = AVL_node(val)
            return

                            # no 'greater than' check as this is the only remaining option: right (= left, inverted)
        if self.right:
            self.right_height += 1
            self.right.insert(val)
            return

        self.right_height += 1
        self.right = AVL_node(val)


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



    def inorder(self,vals):
        # if there's a left, go to it, call inorder recursively
        if self.left is not None:
            self.left.inorder(vals)
            # if there isn't a left, we've reached the next value, so, append it
        if self.val is not None:
            vals.append([self.val,self.left_height,self.right_height])
            # if there is a right child, call recursively
        if self.right is not None:
            self.right.inorder(vals)
            # return what has been gathered from current node (and beneath)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append([self.val,self.left_height,self.right_height])
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals
















if __name__ == "__main__":
    AVL_tree = AVL_node()

    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    for num in nums:
        AVL_tree.insert(num)

    print(AVL_tree.preorder([]))