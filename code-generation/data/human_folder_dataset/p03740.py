import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


X,Y = MI()
print('Alice' if abs(X-Y) >= 2 else 'Brown')
