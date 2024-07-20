def choose_sardines(N, sardines):
    mod = 1000000007
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if sardines[i][0]*sardines[j][0] + sardines[i][1]*sardines[j][1] == 0:
                count += 1
    return count % mod

# Sample Input 1
N = 3
sardines = [(1, 2), (-1, 1), (2, -1)]
print(choose_sardines(N, sardines))

# Sample Input 2
N = 10
sardines = [(3, 2), (3, 2), (-1, 1), (2, -1), (-3, -9), (-8, 12), (7, 7), (8, 1), (8, 2), (8, 4)]
print(choose_sardines(N, sardines))