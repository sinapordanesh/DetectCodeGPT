class Node:
  def __init__(self,key):
    self.key = key
    self.next = None

class List:
  def __init__(self):
    self.head = Node(0)
    self.tail = self.head

  def insert(self,key):
    self.tail.next = Node(key)
    self.tail = self.tail.next

  def dump(self):
    p = self.head.next
    while p != None:
      print(p.key, end='')
      if p.next != None:
        print(' ',end='')
      p = p.next
    print()

  def splice(self,other):
    other.tail.next = self.head.next
    other.tail = self.tail
    self.head.next = None
    self.tail = self.head

''' main function '''
n,q = map(int,input().split())

SList = [List() for i in range(n)]

for i in range(q):
  com,index,*n = map(int,input().split())
  if com == 0:
    SList[index].insert(n[0])
  elif com == 1:
    SList[index].dump()
  elif com == 2:
    SList[index].splice(SList[n[0]])

