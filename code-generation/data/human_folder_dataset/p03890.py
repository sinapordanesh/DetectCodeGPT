#problem3
N=int(input())
from collections import deque
#入力は2**N個からなる
d=[int(input()) for _ in range(2**N)]
def battle(x,y):
    if x!=y:
        return x+y-min(x,y)*2
    else:
        return x
d=deque(d)
for i in range(N):
    for i in range(2**(N-1-i)):
        x=d.popleft()
        y=d.popleft()
        d.append(battle(x,y))
print(d[0])