def compute_XOR(a, b):
    result = 0
    for i in a:
        for j in b:
            result ^= (i + j)
    return result