def coin_combination(N, K, L, R, coins):
    count = 0
    
    def backtrack(total, num_coins, idx):
        nonlocal count
        if num_coins == K:
            if L <= total <= R:
                count += 1
            return
        
        if idx == N:
            return
        
        backtrack(total + coins[idx], num_coins + 1, idx + 1)
        backtrack(total, num_coins, idx + 1)
    
    backtrack(0, 0, 0)
    
    return count

# Sample Input 1
print(coin_combination(2, 2, 1, 9, [5, 1]))

# Sample Input 2
print(coin_combination(5, 2, 7, 19, [3, 5, 4, 2, 2]))