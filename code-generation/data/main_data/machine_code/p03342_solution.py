def count_pairs(N, A):
    count = 0
    for l in range(N):
        xor_sum = 0
        sum = 0
        for r in range(l, N):
            xor_sum ^= A[r]
            sum += A[r]
            if xor_sum == sum:
                count += 1
    return count