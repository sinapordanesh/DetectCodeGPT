def coin_combination(N, V, a, b, c, d):
    count = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if a[i] + b[j] + c[k] + d[l] == V:
                        count += 1
    return count

# Sample Input 1
print(coin_combination(3, 14, [3, 1, 2], [4, 8, 2], [1, 2, 3], [7, 3, 2]))

# Sample Input 2
print(coin_combination(5, 4, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]))