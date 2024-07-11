import sys
input = sys.stdin.readline

def judge():
    l = [10*i+d[i] for i in range(N)]
    
    for i in range(1, N):
        l[i] = max(l[i], l[i-1])
    
    now = 0
    
    for _ in range(N-1):
        now = l[now//10]
        
        if now>=10*(N-1):
            return True
    
    return False

N = int(input())
d = [int(input()) for _ in range(N)]

if judge():
    d.reverse()
    
    if judge():
        print('yes')
        exit()

print('no')
