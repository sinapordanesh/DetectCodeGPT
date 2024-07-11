import sys
from collections import deque


def IN_I(): return int(sys.stdin.readline().rstrip())
def IN_LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def IN_S(): return sys.stdin.readline().rstrip()
def IN_LS(): return list(sys.stdin.readline().rstrip().split())


N = IN_I()
S = IN_S()
d = deque(S)

l = 0
for i in range(N):
    if S[i] == '(':
        l += 1
    else:
        if l == 0:
            d.appendleft('(')
        else:
            l -= 1

r = 0
for i in range(N - 1, -1, -1):
    if S[i] == ')':
        r += 1
    else:
        if r == 0:
            d.append(')')
        else:
            r -= 1
print(''.join(d))
