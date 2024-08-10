def build_altars(N, A, B, C):
    count = 0
    for a in A:
        for b in B:
            for c in C:
                if a < b and b < c:
                    count += 1
    return count

# Sample Input 1
print(build_altars(2, [1, 5], [2, 4], [3, 6]))

# Sample Input 2
print(build_altars(3, [1, 1, 1], [2, 2, 2], [3, 3, 3]))

# Sample Input 3
print(build_altars(6, [3, 14, 159, 2, 6, 53], [58, 9, 79, 323, 84, 6], [2643, 383, 2, 79, 50, 288]))