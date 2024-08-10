def minimum_amount(N, M, prices):
    prices.sort()
    ans = sum(prices)
    for i in range(M):
        if prices[i] < ans:
            ans = ans // 2
        else:
            break
    return ans

# Sample Input 1
print(minimum_amount(3, 3, [2, 13, 8]))

# Sample Input 2
print(minimum_amount(4, 4, [1, 9, 3, 5]))

# Sample Input 3
print(minimum_amount(1, 100000, [1000000000]))

# Sample Input 4
print(minimum_amount(10, 1, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]))