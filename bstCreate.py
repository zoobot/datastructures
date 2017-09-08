# based off this https://github.com/charulagrl/data-structures-and-algorithms/blob/master/data_structures/binary_search_tree.py

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.contains_target = False

class BinarySearchTree(object):
    def __init__(self):
        self.root = None


    def insert(self, data, root):
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
        # send the left node in as the new node
        self.inorder(node.right)

    def contains(self, node, target):
        # if Tree contains target, set to True
        if target == node.data:
            node.contains_target = True
        # otherwise recursively traverse the tree until it is found
        else:
            if target < node.data:
                if node.left:
                    return self.contains(node.left, target)

            elif target > node.data:
                if node.right:
                    return self.contains(node.right, target)

        print(node.data, target)
        return node.contains_target

    def find_largest(self, node):
        if node.right:
            return self.find_largest(node.right)
        return node.data


    def find_smallest(self,node):
        if node.left:
            return self.find_smallest(node.left)
        return node.data

    def tree_max(self, node):
        if not node:
            return float("-inf")
        maxleft  = self.tree_max(node.left)
        maxright = self.tree_max(node.right)
        return max(node.data, maxleft, maxright)

    def tree_min(self, node):
        if not node:
            return float("inf")
        minleft  = self.tree_min(node.left)
        minright = self.tree_min(node.right)
        return min(node.data, minleft, minright)

    def verify(self, node):

        if not node:
            return True
        if (self.tree_max(node.left) <= node.data <= self.tree_min(node.right) and
            self.verify(node.left) and self.verify(node.right)):
            print('inverify', node.data)
            return True
        else:
            return False

    # def bfs(g, root, target):
    #     q = root
    #     while q != None:
    #         current = q.dequeue()
    #     if current == target:
    #         return current
    #     for n in adjacent:
    #         if n != discovered:
    #             n = discovered
    #             n.parent = current
    #             q.enqueue(n)

    def dfselect(filter, node, depth):
        results = []
        if node.right == None and node.left != None:
            results.push(node.data)
            if filter(node.data, depth):
                results.push(node.data)
        for x in node.children:
            child = node.children[i]
            dfselect(child, depth + 1)



    def bfs(root, target):
        q = root, results = [], current_level = [root]
        while current_level:
            current_level = q.dequeue()
            if current_level == target:
                return current_level
            for n in current_level:
                if n != discovered:
                    n = discovered
                    n.parent = current_level
                    q.enqueue(n)

    def breadth_first(root,children=iter):
        """Traverse the nodes of a tree in breadth-first order.
        The first argument should be the tree root; children
        should be a function taking as argument a tree node and
        returning an iterator of the node's children.
        """
        yield tree
        last = tree
        for node in breadth_first(tree,children):
            for child in children(node):
                yield child
                last = child
            if last == node:
                return

    def breadth_first(self,root):
        print("breadth_first root",root.data)
        print("breadth_first root.left",root.left.data)
        print("breadth_first root.right",root.right.data)




class CheckTree():
    def __init__(self,node):
        self.node = None

    def initialize():
        # create a binary search tree
        bst = BinarySearchTree()
        bst.root = bst.insert(4, bst.root)
        bst.insert(55, bst.root)
        bst.insert(9, bst.root)
        bst.insert(2, bst.root)
        # order the Tree inorder
        bst.inorder(bst.root)

        verified = bst.verify(bst.root)
        print("verify", verified)
        # largest should be right most node
        largest = bst.find_largest(bst.root)
        print("Largest node value", largest)
        # smallest should be left most node
        smallest = bst.find_smallest(bst.root)
        print("Smallest node value", smallest)

        bstmax = bst.tree_max(bst.root)
        print("bstmax", bstmax)

        bstmin = bst.tree_min(bst.root)
        print("bstmin", bstmin)

        contains_num = bst.contains(bst.root, 333)
        print("Contains the target number?", contains_num)
        bfs = bst.breadth_first(bst.root)
        print("bfs", bfs)
        return bst


# check whether functions are getting run by this file rather than another module
# if it is being run by this module, __name__ will be __main__
# just run the initialize
if __name__ == "__main__":
    CheckTree.initialize()


# check names this way
# if __name__ == "__main__":
#     Check.initialize()
#     print("__name__"," is ", __name__, "module is run directly")
# else:
#     print("__name__"," is ", __name__, "module is imported into another module")

#Breadth First Search

