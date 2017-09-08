class Node():
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    self.contains_target = False

class BinarySearchTree(object):
  def __init__(self):
    self.root = None

  def insert(self,data,root):
    if root is None:
      return Node(data)

    elif data <= root.data:
      root.left = self.insert(data, root.left)
    else:
      root.right = self.insert(data, root.right)

  def inorder(self, node):
    if node is None:
      return

    self.inorder(node.left)
    print(node.data)
    self.inorder(node.right)

  def contains(self, node, target):
    if target == node.data:
      node.contains_target = True
    else:
      if target < node.data:
        if node.left:
          return self.contains(node.left, target)
      else:
        if node.right:
          return self.contains(node.right, target)
    print(node.data, target)

  def tree_min(self,node):
    if node.left:
      return self.tree_min(node.left)
    return node.data

  def tree_min(self, node):
    if node.right:
      return self.tree_min(node.right)
    return node.data

  def verify(self,node):
    if not node:
      return True
    if self.tree_min(node.left) <= node.data <= self.tree_min(node.right) and self.verify(node.left) and self.verify(node.right):
      return True
    else: return False

  def height(root):
      def sub(tree, depth):
        if root is None:
            return depth - 1
        return max(sub(tree.left, depth+1), sub(tree.right,depth+1))
      sub(root, depth = 0)
