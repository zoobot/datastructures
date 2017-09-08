def BinaryTree(r):
  return [r,[],[]]

def insertLeft(root, newBranch):
  t = root.pop(1)

  if len(t) > 1:
    root.insert(1, [newBranch, t,[]])
  else:
    root.insert(1,[newBranch,[],[]])

def insertRight(root,newBranch):
  t = root.pop(2)
  if len(t) > 1:
    root.insert(2, [newBranch, t,[]])
  else:
    root.insert(2, [newBranch, t,[]])

def getRootVal(root):
  return root[0]

def setRootVal(root,newVal):
  root[0] = newVal


def getLeftChild(root):
  return root[1]

def getRightChild(root):
  return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertRight(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)
print(r)