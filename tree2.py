class BinaryTree(object):
  def __init__(self,rootObj):
    self.key = rootObj
    self.leftChild = None
    self.rightChild = None

  def insertLeft(self, newNode):
    if self.leftChild == None:
      self.leftChild = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.leftChild = self.leftChild
      self.leftChild = t

  def insertRight(self, newNode):
    if self.rightChild == None:
      self.rightChild = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.rightChild = self.rightChild
      self.rightChild = t

  def getRightChild(self):
    return self.rightChild

  def getLeftChild(self):
    return self.rightChild

  def setRootVal(self,obj):
    set.key = obj

  def getRootVal(self):
    return self.key

  def getLeftChild(self):
    return self.leftChild

  def setRootVal(self,obj):
    self.key = obj

  def getRootVale(self):
    return self.key

def inorder(tree):
  if tree != None:
    inorder(tree.getLeftChild())
    print(tree.getRootVal())
    inorder(tree.getRightChild())

def preorder(tree):
  if tree != None:
    print(tree.getRootVal())
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())

def postorder(tree):
  if tree != None:
    postorder(tree.getLeftChild())
    postorder(tree.getRightChild())
    print(tree.getRootVal())

def breadth_first(tree):
  queue = tree

  while queue is not None:
    traverse = queue.remove()

    if traverse.getLeftChild() is not None:
      queue.insert(traverse.getLeftChild())
    if traverse.getRightChild() is not None:
      queue.insert(traverse.getRightChild())

def delete(data):
    node, parent = self.lookup(data)
    if node is not None:
      children_count = node.children_count()
    if children_count == 0:
      if parent:
        if parent.left is node:
          parent.left = None
        else:
          parent.right = None
      else:
        self.data = None
    elif children_count == 1:
      if node.left:
        n = node.left
      else:
        n = node.right
      if parent:
        if parent.left is node:
          parent.left = n
        else:
         parent.right = n
        del node
      else:
        self.left = n.left
        self.right = n.right
        self.data = n.data


newTree = BinaryTree(0)
newTree.insertLeft(1)
newTree.insertLeft(2)
newTree.insertLeft(3)
newTree.insertLeft(4)
newTree.insertRight(5)
# inorder(newTree)
# print('\n')
# preorder(newTree)
# print('\n')
# postorder(newTree)
breadth_first(newTree)
# print(10//2)
# print(10//3)
# print(10/3)
# print(10/2)