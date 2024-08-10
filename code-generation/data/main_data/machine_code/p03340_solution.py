def count_pairs(A):
    count = 0
    for i in range(len(A)):
        xor_sum = 0
        sum = 0
        for j in range(i, len(A)):
            xor_sum ^= A[j]
            sum += A[j]
            if xor_sum == sum:
                count += 1
    return count