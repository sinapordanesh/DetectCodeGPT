def max_layers(N, diameters):
    unique_diameters = set(diameters)
    return len(unique_diameters)

# Sample Input 1
print(max_layers(4, [10, 8, 8, 6]))

# Sample Input 2
print(max_layers(3, [15, 15, 15]))

# Sample Input 3
print(max_layers(7, [50, 30, 50, 100, 50, 80, 30]))