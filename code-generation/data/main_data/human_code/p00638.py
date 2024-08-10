from sys import exit
from functools import reduce
from operator import add
def f(): return [int(i) for i in input().split()]

while True:
    flag = False
    n = int(input())
    if not(n):
        exit()
    islands = []
    for i in range(n):
        islands.append(f())
    islands.sort(key=lambda x:x[1])
    
    weight = 0
    for j in range(n):
        weight += islands[j][0]
        if weight > islands[j][1]:
            flag = True
            print("No")
            break
    if not(flag):
        print("Yes")    
