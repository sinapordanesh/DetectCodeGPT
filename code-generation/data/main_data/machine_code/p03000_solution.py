def num_bounces(N, X, L):
    count = 1
    total = 0
    for i in range(N):
        total += L[i]
        if total <= X:
            count += 1
    return count

# Sample Input 1
print(num_bounces(3, 6, [3, 4, 5]))

# Sample Input 2
print(num_bounces(4, 9, [3, 3, 3, 3]))