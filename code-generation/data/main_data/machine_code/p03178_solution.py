def count_integers(K, D):
    count = 0
    for i in range(1, K+1):
        digit_sum = sum(map(int, str(i)))
        if digit_sum % D == 0:
            count += 1
    return count % (10**9 + 7)