def min_same_cake_days(K, T, cakes):
    max_cakes = max(cakes)
    total_cakes = sum(cakes)
    
    if max_cakes * 2 <= total_cakes:
        return 0
    else:
        return max_cakes - (total_cakes - max_cakes)

# Read input values
K, T = map(int, input().split())
cakes = list(map(int, input().split()))

# Call the function and print the result
print(min_same_cake_days(K, T, cakes))