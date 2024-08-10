def max_consecutive_hands(N, K, S):
    max_consecutive = S.count('1')
    current_consecutive = 0
    for i in range(N):
        if S[i] == '1':
            current_consecutive += 1
        else:
            if K > 0:
                current_consecutive += 1
                K -= 1
            else:
                current_consecutive = 0
        max_consecutive = max(max_consecutive, current_consecutive)
    return max_consecutive

# Sample Input 1
print(max_consecutive_hands(5, 1, '00010'))

# Sample Input 2
print(max_consecutive_hands(14, 2, '11101010110011'))

# Sample Input 3
print(max_consecutive_hands(1, 1, '1'))