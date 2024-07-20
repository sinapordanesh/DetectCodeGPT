def max_num_operations(N):
    ans = 0
    i = 2
    while i*i <= N:
        if N % i == 0:
            ans += 1
            N //= i
            while N % i == 0:
                N //= i
        i += 1
    if N != 1:
        ans += 1
    return ans

N = int(input())
print(max_num_operations(N))