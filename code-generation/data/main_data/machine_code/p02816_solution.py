def find_pairs(N, a, b):
    res = []
    for k in range(N):
        x = a[0] ^ b[k]
        valid = True
        for i in range(N):
            if a[(i+k)%N] ^ x != b[i]:
                valid = False
                break
        if valid:
            res.append((k, x))
    for pair in sorted(res):
        print(pair[0], pair[1]) 

# Sample Input 1
find_pairs(3, [0, 2, 1], [1, 2, 3])

# Sample Input 2
find_pairs(5, [0, 0, 0, 0, 0], [2, 2, 2, 2, 2])

# Sample Input 3
find_pairs(6, [0, 1, 3, 7, 6, 4], [1, 5, 4, 6, 2, 3])

# Sample Input 4
find_pairs(2, [1, 2], [0, 0])