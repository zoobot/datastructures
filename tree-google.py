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