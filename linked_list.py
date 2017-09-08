# singly linked list
# tail.next = None is tail

# insert at head
# create new node
# set element to new element
# set next link to refer to the current head
# set list head to point to new node

# insert at tail
# create new node
# assign next to None
#set next reference of the tail to point to new node
# update tail reference to new node


class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None

def reverse(head):
  # 1,2,3,4
  print(head.value)
  current = head
  previous = None
  nextnode = None

  while current:
    nextnode = current.nextnode
    current.nextnode = previous
    previous = current
    current = nextnode

    # head.temp = head.value
    # head.value = head.nexthead.value
    # node.nextnode.value = node.temp

  # print(head.value)
  return previous

# def print_list(self):
#     print('self.head.data',self.head.data)

#     if self.head == None:
#       print("List is empty")

#     current = self.head
#     while current:
#       print(current.data, end=' ')
#       current = current.next_node
#     print('\n')

def nth_to_last_node(n, head):
  if head is None:
    return
  node_pointer = head
  main_pointer = head
  count = 0
  while count < n:
      node_pointer = node_pointer.nextnode
      count += 1

  while node_pointer:
    node_pointer = node_pointer.nextnode
    main_pointer = main_pointer.nextnode

  return main_pointer.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
# print('reverse(a)',reverse(a))
# print('a.value',a.value)
# print('d.nextnode.value',d.nextnode.value)
# print('c.nextnode.value',c.nextnode.value)
# print('b.nextnode.value',b.nextnode.value)
# print(a.nextnode.value, '\n')

target_node = nth_to_last_node(3, a)
print(target_node)

# constant time insertion and deletion
# can resize

# Pros and constant
# Pros
# Linkedlist have constant time insertion and deletionat any position, arrays require o(n)
# Linkedlist can resize without having to specify size ahead of time

# cons
# to access element you need to take O(k) time to go from head to kth element, arrays have constant time operations to access elements in an array

# class DoublyLinkedListNode(object):
#   def __init__(self,value):
#     self.value = value
#     self.nextnode = None
#     self.prevnode = None

# def cycle_check(node):
#   marker1 = node
#   marker2 = node
#   while marker2 != None and marker2.nextnode != None:
#     marker1 = marker1.nextnode
#     marker2 = marker2.nextnode.nextnode
#     if marker2 == marker1:
#       return True
#   return False

# a = DoublyLinkedListNode(1)
# b = DoublyLinkedListNode(2)
# c = DoublyLinkedListNode(3)

# a.nextnode = b
# b.prevnode = a
# b.nextnode = c
# c.prevnode = b
# #for circular linked list
# c.nextnode = a
# a.prevnode = c

# print(cycle_check(a))

