import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    
    not_yet = deque([0])
    already = [False]*n
    already[0] = True
    dist = [0]*n

    while not_yet:
        value = not_yet.popleft()
        for v in tree[value]:
            if already[v]:
                continue
            already[v] = True
            dist[v] = (dist[value] + 1) % 2
            not_yet.append(v)
    
    zero = dist.count(0)
    one = dist.count(1)

    ans = [0]*n
    already = [False]*n
    if zero >= one:
        if one <= n//3:
            ind = 1
            for i in range(n):
                if dist[i] == 1:
                    ans[i] = ind*3
                    already[ind*3-1] = True
                    ind += 1
            ind = 0
            for i in range(n):
                if ans[i] == 0:
                    while already[ind]:
                        ind += 1
                    ans[i] = ind + 1
                    already[ind] = True
    
        else:
            c0, c1, c2 = 0, 0, 1
            z, o = n//3 + bool(n%3), n//3 + bool(n%3==2)
            for i in range(n):
                if dist[i] == 0:
                    if c0 >= z:
                        ans[i] = c2*3
                        c2 += 1
                        continue
                    ans[i] = c0*3 + 1
                    c0 += 1
                else:
                    if c1 >= o:
                        ans[i] = c2*3
                        c2 += 1
                        continue
                    ans[i] = c1*3 + 2
                    c1 += 1
    else:
        if zero <= n//3:
            ind = 1
            for i in range(n):
                if dist[i] == 0:
                    ans[i] = ind*3
                    already[ind*3-1] = True
                    ind += 1
            ind = 0
            for i in range(n):
                if ans[i] == 0:
                    while already[ind]:
                        ind += 1
                    ans[i] = ind + 1
                    already[ind] = True
    
        else:
            c0, c1, c2 = 0, 0, 1
            z, o = n//3 + bool(n%3), n//3 + bool(n%3==2)
            for i in range(n):
                if dist[i] == 1:
                    if c0 >= z:
                        ans[i] = c2*3
                        c2 += 1
                        continue
                    ans[i] = c0*3 + 1
                    c0 += 1
                else:
                    if c1 >= o:
                        ans[i] = c2*3
                        c2 += 1
                        continue
                    ans[i] = c1*3 + 2
                    c1 += 1

    print(*ans)

            


    
if __name__ == "__main__":
    main()

