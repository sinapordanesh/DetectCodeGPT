def min_mod_2019(L, R):
    min_mod = float('inf')
    for i in range(L, R):
        for j in range(i+1, R+1):
            mod = (i*j) % 2019
            min_mod = min(mod, min_mod)
    return min_mod

# Sample Input 1
print(min_mod_2019(2020, 2040))

# Sample Input 2
print(min_mod_2019(4, 5))