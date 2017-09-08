

def walker(node, low = None, high = None):
    if node == None:
        return True
    if low is not None and low >= node.data:
        return False
    if high is not None and high <= node.data:
        return False
    return walker(node.left, low, node.data)

def least(node):
    if node.left is None:
        return node.data
    return least(node.left)

def most(node):
    if node.right is None:
        return node.data
    return most(node.right)

def checkBST(root):
    if root == None:
        return True
    return walker(root)

'''
If the tree is not valid, there will be a smaller value s somewhere in the tree such that s < least(root), and/or a larger value l somewhere in the tree such that most(root) < l. Either of these will fail the (low < node.data < high) validation step.
'''


def checkBST(root):
    if root == None:
        return True
    return walker(root)

root = new Node()
checked = checkBST(root)
print(checked)

