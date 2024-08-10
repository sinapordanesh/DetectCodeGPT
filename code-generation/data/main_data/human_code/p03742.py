import sys

def S(): return sys.stdin.readline().rstrip()

X,Y = map(int,S().split())

if abs(X-Y) <= 1:
    print('Brown')
else:
    print('Alice')