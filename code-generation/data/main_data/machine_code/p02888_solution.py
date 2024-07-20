def count_triangles(N, sticks):
    sticks.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                a = sticks[i]
                b = sticks[j]
                c = sticks[k]
                if a < b + c and b < c + a and c < a + b:
                    count += 1
    return count

# Sample Input 1
print(count_triangles(4, [3, 4, 2, 1]))

# Sample Input 2
print(count_triangles(3, [1, 1000, 1]))

# Sample Input 3
print(count_triangles(7, [218, 786, 704, 233, 645, 728, 389]))