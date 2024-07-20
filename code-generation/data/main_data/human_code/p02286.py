# -*- coding: utf-8 -*-

class Node:
  def __init__(self, key, priority, left=None, right=None):
    self.key = key
    self.priority = priority
    self.left = left
    self.right = right
  
def rightRotate(t):
  s = t.left
  t.left = s.right
  s.right = t
  return s

def leftRotate(t):
  s = t.right
  t.right = s.left
  s.left = t
  return s

def insert(t, key, priority):
  
  if not t: return Node(key, priority)
  if key == t.key: return t
  
  if key < t.key: 
    t.left = insert(t.left, key, priority)
    if t.priority < t.left.priority:
      t = rightRotate(t)
  else:
    t.right = insert(t.right, key, priority)
    if t.priority < t.right.priority:
      t = leftRotate(t)
  
  return t

def erase(t, key):
  
  if not t: return None
  
  if key == t.key:
    if (not t.left) and (not t.right): return None
    elif not t.left: 
      t = leftRotate(t)
    elif not t.right:
      t = rightRotate(t)
    else:
      if t.left.priority > t.right.priority:
        t = rightRotate(t)
      else:
        t = leftRotate(t)
    return erase(t, key)
  elif key > t.key:
    t.right = erase(t.right, key)
  else:
    t.left = erase(t.left, key)
  return t


def find(t, key):
  if t.key == key:
    print("yes")
  elif t.key < key and t.right != None:
    find(t.right, key)
  elif t.key > key and t.left != None:
    find(t.left, key)
  else:
    print("no")
  return 0

def in_print(t):
  if t.left != None:
    in_print(t.left)
  print(" " + str(t.key), end='')
  if t.right != None:
    in_print(t.right)

def pre_print(t):
  print(" " + str(t.key), end='')
  if t.left != None:
    pre_print(t.left)
  if t.right != None:
    pre_print(t.right)
  
Treap = None
num = int(input())
for i in range(num):
  string = list(input().split())
  if string[0] == "insert":
    key = int(string[1])
    priority = int(string[2])
    Treap = insert(Treap, key, priority)
  elif string[0] == "find":
    key = int(string[1])
    find(Treap, key)
  elif string[0] == "delete":
    key = int(string[1])
    Treap = erase(Treap, key)
  else:
    in_print(Treap)
    print()
    pre_print(Treap)
    print()
    

  
