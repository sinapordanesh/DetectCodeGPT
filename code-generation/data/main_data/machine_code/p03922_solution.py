def maximum_pairs(N, M, cards):
    count = [0] * M
    for card in cards:
        count[card % M] += 1
    ans = min(count[0], 1)
    for i in range(1, (M+1)//2):
        ans += max(count[i], count[M-i])
    if M % 2 == 0:
        ans += min(count[M//2], 1)
    return ans

# Sample Input 1
print(maximum_pairs(7, 5, [3, 1, 4, 1, 5, 9, 2]))

# Sample Input 2
print(maximum_pairs(15, 10, [1, 5, 6, 10, 11, 11, 11, 20, 21, 25, 25, 26, 99, 99, 99]))