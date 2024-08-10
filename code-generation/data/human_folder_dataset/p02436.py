class Node:
  def __init__(self,key):
    self.key = key
    self.prev = None
    self.next = None

class Queue:
  def __init__(self):
    self.head = Node(0)
    self.tail = self.head

  def enqueue(self,key):
    node = Node(key)
    self.tail.next = node
    node.prev = self.tail
    self.tail = node

  def front(self):
    if self.head != self.tail:
      return self.head.next.key

  def dequeue(self):
    if self.head != self.tail:
      if self.head.next == self.tail:
        self.tail = self.head
      self.head.next = self.head.next.next


n,q = map(int,input().split())

Q = [Queue() for i in range(n)]

for i in range(q):
  com, index, *n = map(int,input().split())
  if com == 0:
    Q[index].enqueue(*n)
  elif com == 1:
    key = Q[index].front()
    if key != None:
      print(key)
  elif com == 2:
    Q[index].dequeue()

