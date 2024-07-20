# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:51:44 2018

@author: maezawa
"""

class node():
    def __init__(self, key, parent=None, right=None, left=None):
        self.key = key
        self.parent = parent
        self.right = right
        self.left = left
        
def insert(z):
    global root
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z  
    #inorder(root)
    
def find(x, k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x

def delete_node(z):
    global root
    #x = node(None)
    if z.left == None or z.right == None:
        y = z
    else:
        y = get_successor(z)
        
    if y.left != None:
        x = y.left
    else:
        x = y.right
    if x != None:
        x.parent = y.parent

    if y.parent == None:
        root = x
        #print('deleteing {}, settting the root for {}'.format(y.key,x))
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    if y != z:
        z.key = y.key
        
def get_successor(x):
    if x.right != None:
        return get_min(x.right)
    y = x.parent
    while y != None and x == y.right:
        x = y
        y = y.parent
    return y

def get_min(x):
    while x.left != None:
        x = x.left
    return x
        
def inorder(u):
    if u == None:
        return
    inorder(u.left)
    print(' {}'.format(u.key), end = '')
    inorder(u.right)
    
def preorder(u):
    if u == None:
        return
    print(' {}'.format(u.key), end = '')
    preorder(u.left)
    preorder(u.right)
    
root = None

n = int(input())
for i in range(n):
    q = list(input().split())
    if q[0] == 'insert':
        z = node(int(q[1]))
        insert(z)
    elif q[0] == 'find':
        if find(root, int(q[1])):
            print('yes')
        else:
            print('no')
    elif q[0] == 'delete':
            z = find(root, int(q[1]))
            delete_node(z)
    elif q[0] == 'print':
        inorder(root)
        print()
        preorder(root)
        print()
    #print('root:{}'.format(root.key))
        
        
