def count_possible_assignments(dataset):
    MOD = 1000000007
    A, B, C = dataset
    count = 1
    for a, b, c in zip(A, B, C):
        if a == '?' and b == '?' and c == '?':
            count = (count * 10) % MOD
        elif a == '?' and b == '?':
            count = (count * 10) % MOD
        elif a == '?' and c == '?':
            count = (count * 10) % MOD
        elif b == '?' and c == '?':
            count = (count * 10) % MOD
    return count % MOD