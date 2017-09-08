# https://github.com/charulagrl/data-structures-and-algorithms/blob/master/data_structures/binary_search_tree.py

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.list = []

class BinarySearchTree(object):
    def __init__(self):
        self.root = None


    def insert(self, data, root):
        # print(self)
        # for i in self:
        #     print(i)
        # if there is no root node, make one
        if root is None:
            return Node(data)

        # if there is a root node then check if data is less that the root and add to left node
        elif data <= root.data:
            root.left = self.insert(data, root.left)
        # otherwise add data the right node
        else:
            root.right = self.insert(data, root.right)
        # return the tree
        return root

    def inorder(self, node):
        # Print inorder tree traversal
        if node is None:
            return

        # send the left node in as the new node
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

def initialize():
    # create a binary search tree

    bst = BinarySearchTree()
    bst.root = bst.insert(6, bst.root)
    bst.insert(1, bst.root)
    bst.insert(9, bst.root)
    bst.insert(3, bst.root)
    bst.inorder(bst.root)
    return bst

# check whether functions are getting run by this file rather than another module
# if it is being run by this module, __name__ will be __main__
if __name__ == "__main__":
    print(__name__)
    initialize()