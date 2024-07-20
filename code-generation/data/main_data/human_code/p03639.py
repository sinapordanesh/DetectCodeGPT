import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

one = 0
two = 0
four = 0
for i in range(N):
    a = As[i]
    if a%4==0:
        four += 1
    elif a%2==0:
        two += 1
    else:
        one += 1
if one==0:
    print('Yes')
elif one==1:
    if four>=1:
        print('Yes')
    else:
        print('No')
else:
    if one+four==N and four>=one-1:
        print('Yes')
    else:
        if four>=one:
            print('Yes')
        else:
            print('No')
    