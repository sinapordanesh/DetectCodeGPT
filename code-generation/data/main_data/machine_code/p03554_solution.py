def min_hamming_distance(N, b, Q, operations):
    a = [0] * N
    hamming_dist = 0
    
    for l, r in operations:
        for i in range(l-1, r):
            a[i] = 1
        hamming_dist = sum([1 for i in range(N) if a[i] != b[i]])
    
    return hamming_dist

# Test the function with the provided sample inputs
print(min_hamming_distance(3, [1, 0, 1], 1, [(1, 3)]))
print(min_hamming_distance(3, [1, 0, 1], 2, [(1, 1), (3, 3)]))
print(min_hamming_distance(3, [1, 0, 1], 2, [(1, 1), (2, 3)]))
print(min_hamming_distance(5, [0, 1, 0, 1, 0], 1, [(1, 5)]))
print(min_hamming_distance(9, [0, 1, 0, 1, 1, 1, 0, 1, 0], 3, [(1, 4), (5, 8), (6, 7)]))
print(min_hamming_distance(15, [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0], 9, [(4, 10), (13, 14), (1, 7), (4, 14), (9, 11), (2, 6), (7, 8), (3, 12), (7, 13)]))
print(min_hamming_distance(10, [0, 0, 0, 1, 0, 0, 1, 1, 1, 0], 7, [(1, 4), (2, 5), (1, 3), (6, 7), (9, 9), (1, 5), (7, 9)]))