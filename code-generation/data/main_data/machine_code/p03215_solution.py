def max_bitwise_and(N, K, a):
    max_val = 0
    for i in range(N):
        for j in range(i, N):
            beauty = sum(a[i:j+1])
            max_val = max(max_val, beauty)
    return max_val

N, K = map(int, input().split())
a = list(map(int, input().split()))

print(max_bitwise_and(N, K, a))