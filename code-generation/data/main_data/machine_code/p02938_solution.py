def find_pairs(L, R):
    MOD = 10**9 + 7
    count = 0
    for x in range(L, R+1):
        for y in range(x, R+1):
            if (y % x) == (y ^ x):
                count += 1
    return count % MOD

# Sample Input 1
print(find_pairs(2, 3))

# Sample Input 2
print(find_pairs(10, 100))

# Sample Input 3
print(find_pairs(1, 1000000000000000000))