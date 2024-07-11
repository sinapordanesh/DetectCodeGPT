N = int(input())

if N == 2:
    print(2, 3)
    print(5, 4)
    exit()

a = [[1] * N for _ in range(N)]

PN = [2]
L = 3
while len(PN) < N*2:
    c = True
    for p in PN:
        if L % p == 0: c = False
    if c == True: PN.append(L)
    L += 2

def P1(k):
    return PN[(k//2)]

def P2(k):
    if k >= 0:
        return PN[(k//2) + N]
    else:
        return PN[(k//2)]

for i in range(N):
    for j in range(N):
        if (i + j) % 2 == 0:
            a[i][j] = P1(i + j) * P2(i - j)
        else:
            a[i][j] += P1(i + j + 1) * P1(i + j - 1) * P2(i - j + 1) * P2(i - j - 1)

for a_i in a:
    print(*a_i)
