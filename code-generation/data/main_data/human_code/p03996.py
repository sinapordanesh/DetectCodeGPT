import sys
readline = sys.stdin.readline

import sys
from itertools import product
readline = sys.stdin.readline

def check1(A):
    K = max(A)
    table = [-1]*(K+1)
    for i in range(Q):
        table[A[i]] = i
    
    if -1 in table:
        return False
    if any(t1-t2 < 0 for t1, t2 in zip(table, table[1:])):
        return False
    return True

INF = 10**9+7
def check2(A):
    stack = []
    used = set()
    for a in A[::-1] + list(range(M)):
        if a not in used:
            used.add(a)
            stack.append(a)
    
    C = dict()
    for i in range(M):
        C[stack[i]] = i
    
    table = [0]*M + [INF]
    for a in A[::-1]:
        if table[C[a]] < table[C[a]-1]:
            table[C[a]] += 1
    
    used = set()
    ch = []
    for i in range(M):
        if table[i] < N:
            break
        ch.append(stack[i])
        used.add(stack[i])
    for i in range(M):
        if i not in used:
            used.add(i)
            ch.append(i)
    
    return stack == ch

N, M = map(int, readline().split())
Q = int(readline())
A = list(map(lambda x: int(x)-1, readline().split()))

ans = 'Yes'
if not check1(A):
    if not check2(A):
        ans = 'No'
print(ans)