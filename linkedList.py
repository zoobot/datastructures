class Node:
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node


class LinkedList:
  def __init__(self, head=None):
    self.head = head


  def addToTail(self,data):
    node = Node(data)
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.next_node = node
      self.tail = node

  def insert(self, data):
    node = Node(data)
    if not self.head:
      self.head = node
    else:
      node.next_node = self.head
      self.head = node

  def delete(self, data):
    current = self.head
    if not self.head:
      return
    while current:
      if current.data == data:
        head = current.next_node
        print("Deleted node is if1", current.data)
        return
      if current.next_node.data == data:
      # else:
        # print("Deleted node: ", current.data)
        current = current.next_node
        print("Deleted node: ", current.next_node.data)
        return
      current = current.next_node
    print("Node not found")
    return

  def removeHead(self):
    if self.head == self.tail:
      self.tail = None
    self.head = self.head.next_node

  def search(self,target):
    current = self.head
    while current:
      if current.data == target:
        return True
      else:
        current = current.next_node
    return False

  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next_node
    return count

  def print_list(self):
    print('self.head.data',self.head.data)

    if self.head == None:
      print("List is empty")

    current = self.head
    while current:
      print(current.data, end=' ')
      current = current.next_node
    print('\n')

  def reverse(self):
    print(self.head.data)
    current = self.head

    previous = None
    next_node = None
    while current:
      next_node = current.next_node
      current.next_node = previous
      previous = current
      current = next_node
    print(previous)
    return previous


node = LinkedList()
node.addToTail(1)
node.addToTail(4)
node.addToTail("tttttt")
node.addToTail(13)
node.addToTail(333)
node.addToTail(555)

# print(node.search("tttttt"))
print(node.size())
# print(node.delete("tttttt"))
# print(node.delete(333))
# print(node.delete(555))

# print(node.removeHead())
node.reverse()
node.print_list()