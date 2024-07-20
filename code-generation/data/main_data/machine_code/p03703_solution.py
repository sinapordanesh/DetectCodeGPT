def count_subsequences(N, K, a):
    count = 0
    for i in range(N):
        for j in range(i, N):
            subseq = a[i:j+1]
            mean = sum(subseq) / len(subseq)
            if mean >= K:
                count += 1
    return count

# Sample Input 1
print(count_subsequences(3, 6, [7, 5, 7]))

# Sample Input 2
print(count_subsequences(1, 2, [1]))

# Sample Input 3
print(count_subsequences(7, 26, [10, 20, 30, 40, 30, 20, 10]))