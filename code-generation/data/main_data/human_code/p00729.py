# coding: utf-8
# Your code here!

def solve(N, M):
    login = [0] * (M+1)
    student = [[] for i in range(M+1)]
    r = int(input())
    for i in range(r):
        t, n, m, s = map(int, input().split())
        if s == 1:
            if login[m] == 0:
                student[m].append(t)
            login[m] += 1
        else:
            login[m] -= 1
            if login[m] == 0:
                student[m].append(t)
    q = int(input())
    for i in range(q):
        s, e, m = map(int, input().split())
        ans = 0
        for j in range(0, len(student[m]), 2):
            s2 = student[m][j]
            e2 = student[m][j+1]
            l = max(s, s2)
            r = min(e, e2)
            if r - l > 0:
                ans += r - l
        print(ans)
            
while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    solve(N, M)
