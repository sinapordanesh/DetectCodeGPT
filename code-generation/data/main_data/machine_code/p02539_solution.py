def count_pairs(N, heights):
    MOD = 998244353
    pairs = 1
    count = {}
    
    for height in heights:
        if height not in count:
            count[height] = 1
        else:
            count[height] += 1
    
    for i in range(1, N+1):
        pairs = (pairs * (2*i - count.get(i, 0))) % MOD
    
    return pairs

#Sample Input
N = 2
heights = [1, 1, 2, 3]
print(count_pairs(N, heights))

N = 5
heights = [30, 10, 20, 40, 20, 10, 10, 30, 50, 60]
print(count_pairs(N, heights))