#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    def parse_winner(s,i):
        if s[i] == "[":
            i += 1
            w1, i = parse_winner(s,i)
            i += 1
            w2, i = parse_winner(s,i)
            return calc(w1, w2), i+1
        else:
            p, i = parse_person(s,i)
            return p, i

    def parse_person(s,i):
        return s[i], i+1

    def calc(w1,w2):
        if f[w1] == 0:
            if f[w2] == 0:
                return "0"
            else:
                f[w2] -= 1
                return w2
        else:
            if f[w2] != 0:
                return "0"
            else:
                f[w1] -= 1
                return w1

    s = S()
    k = 0
    for i in s:
        if i not in "[-]":
            k += 1
    f = defaultdict(int)
    f["0"] = 100000
    for i in range(k):
        a,b = input().split()
        f[a] = int(b)
    w = parse_winner(s,0)[0]
    if f[w]:
        print("No")
    else:
        print("Yes")
    return

#B
def B():
    n,k = LI()
    s = S()
    t = S()
    q = deque()
    ans = 0
    for i in range(n):
        if s[i] == "B" and t[i] == "W":
            if q:
                x = q.popleft()
                if i-x >= k:
                    ans += 1
                    while q:
                        q.popleft()
            q.append(i)
    if q:
        ans += 1
    for i in range(n):
        if s[i] == "W" and t[i] == "B":
            if q:
                x = q.popleft()
                if i-x >= k:
                    ans += 1
                    while q:
                        q.popleft()
            q.append(i)
    if q:
        ans += 1
    print(ans)
    return

#C
def C():
    n = I()
    s = SR(n)
    t = S()

    return

#D
from operator import mul
def D():
    def dot(a,b):
        return sum(map(mul,a,b))
    def mul_matrix(a,b,m):
        tb = tuple(zip(*b))
        return [[dot(a_i,b_j)%m for b_j in tb] for a_i in a]

    def pow_matrix(a,n,m):
        h = len(a)
        b = [[1 if i == j else 0 for j in range(h)] for i in range(h)]
        k = n
        while k:
            if (k&1):
                b = mul_matrix(b,a,m)
            a = mul_matrix(a,a,m)
            k >>= 1
        return b
    while 1:
        n,m,a,b,c,t = LI()
        if n == 0:
            break
        s = LI()
        s2 = [[s[i] for j in range(1)] for i in range(n)]
        mat = [[0 for j in range(n)] for i in range(n)]
        mat[0][0] = b
        mat[0][1] = c
        for i in range(1,n-1):
            mat[i][i-1] = a
            mat[i][i] = b
            mat[i][i+1] = c
        mat[n-1][-2] = a
        mat[n-1][-1] = b
        mat = pow_matrix(mat,t,m)
        mat = mul_matrix(mat,s2,m)
        for i in mat[:-1]:
            print(i[0],end = " ")
        print(mat[-1][0])
    return


#E
def E():
    def surface(x,y,z):
        return ((x == 0)|(x == a-1))+((y == 0)|(y == b-1))+((z == 0)|(z == c-1))+k

    d = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    a,b,c,n = LI()
    s = [0 for i in range(7)]
    k = (a==1)+(b==1)+(c==1)
    if k == 0:
        s[1] = 2*(max(0,a-2)*max(0,b-2)+max(0,c-2)*max(0,b-2)+max(0,a-2)*max(0,c-2))
        s[2] = 4*(max(0,a-2)+max(0,b-2)+max(0,c-2))
        s[3] = 8
    elif k == 1:
        s[2] = max(0,a-2)*max(0,b-2)+max(0,c-2)*max(0,b-2)+max(0,a-2)*max(0,c-2)
        s[3] = 2*(max(0,a-2)+max(0,b-2)+max(0,c-2))
        s[4] = 4
    elif k == 2:
        s[4] = max(0,a-2)+max(0,b-2)+max(0,c-2)
        s[5] = 2
    else:
        s[6] = 1
    f = defaultdict(int)
    for i in range(n):
        x,y,z = LI()
        s[surface(x,y,z)] -= 1
        f[(x,y,z)] = -1
        for dx,dy,dz in d:
            if f[(x+dx,y+dy,z+dz)] != -1:
                f[(x+dx,y+dy,z+dz)] += 1
    ans = 0
    for i,j in f.items():
        if j != -1:
            x,y,z = i
            if 0 <= x < a and 0 <= y < b and 0 <= z < c:
                ans += j+surface(x,y,z)
                s[surface(x,y,z)] -= 1
    for i in range(1,7):
        ans += i*s[i]
    print(ans)
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    A()

