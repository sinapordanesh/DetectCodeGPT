def restore_scarf_integers(N, a):
    x = 0
    for i in range(N):
        x ^= a[i]
    
    result = []
    for i in range(N):
        result.append(x ^ a[i])
    
    return result

# Sample Input
N = 4
a = [20, 11, 9, 24]
print(*restore_scarf_integers(N, a))