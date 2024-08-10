def construct_sequences(N, p):
    a = [0]*N
    b = [0]*N
    for i in range(N):
        a[p[i]-1] = 10**9 - 1 - i
    for i in range(N):
        b[p[i]-1] = 10**9 - N + i
    return a, b

N = int(input())
p = list(map(int, input().split()))
a, b = construct_sequences(N, p)
print(*a)
print(*b)