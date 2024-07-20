def max_pairs(N, M, X):
    count = [0] * M
    for x in X:
        count[x % M] += 1
    
    result = min(count[0], 1)
    for i in range(1, (M+1)//2):
        if i != M - i:
            result += min(count[i], count[M-i])
        else:
            result += min(count[i], 1)
    
    if M % 2 == 0:
        result += min(count[M//2], 1)
    
    return result

# Sample Input 1
print(max_pairs(7, 5, [3, 1, 4, 1, 5, 9, 2])) # 3

# Sample Input 2
print(max_pairs(15, 10, [1, 5, 6, 10, 11, 11, 11, 20, 21, 25, 25, 26, 99, 99, 99])) # 6