# n= 人数　p = 最初に入っている個数

def solve(n, p):
    tmp = p
    i = 0
    person = [0] * n
    while(1):
        if tmp != 0:
            person[i] += 1
            tmp -= 1
            if person[i] == p:
                return i
        else:
            tmp = person[i]
            person[i] = 0

        i += 1
        if i == n:
            i = 0

ans = []
while(1):
    n, p = map(int,input().split())
    if n == 0 and p == 0:
        for i in ans:
            print(i)

        break
    else:
        ans.append(solve(n, p))

