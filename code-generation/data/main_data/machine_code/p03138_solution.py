def max_xor_sum(N, arr, K):
    max_val = 0
    for i in range(K+1):
        total = 0
        for num in arr:
            total += i ^ num
        max_val = max(max_val, total)
    return max_val