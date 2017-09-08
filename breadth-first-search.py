def bfs(g, root, target):
  q = root
  while q != None:
    current = q.dequeue()
    if current == target:
      return current
    for n in adjacent:
      if n is not discovered allready:
        n = discovered
        n.parent = current
        q.enqueue(n)


def breadth_first(self,root)
  queue = root

  while queue is not Empty:
    traverse = queue.remove()

    if traverse.get