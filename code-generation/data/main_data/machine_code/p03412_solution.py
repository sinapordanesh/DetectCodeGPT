def compute_XOR(a, b):
    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            result ^= a[i] + b[j]
    return result