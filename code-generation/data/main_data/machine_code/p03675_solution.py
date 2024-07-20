def sequence_b(n, a):
    b = []
    for i in range(n):
        b.append(a[i])
        b = b[::-1]
    return b

n = int(input())
a = list(map(int, input().split()))
result = sequence_b(n, a)
print(*result)