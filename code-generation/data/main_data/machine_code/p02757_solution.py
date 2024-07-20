def count_substrings(N, P, S):
    count = 0
    for i in range(N):
        num = 0
        for j in range(i, N):
            num = num * 10 + int(S[j])
            if num % P == 0:
                count += 1
    return count

# Sample Input 1
print(count_substrings(4, 3, '3543'))

# Sample Input 2
print(count_substrings(4, 2, '2020'))

# Sample Input 3
print(count_substrings(20, 11, '33883322005544116655'))