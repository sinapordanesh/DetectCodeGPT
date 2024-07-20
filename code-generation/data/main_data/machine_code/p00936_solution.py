def squeeze_cylinders(N, radii):
    radii.sort()
    max_distance = 2 * radii[-1]
    return max_distance

# Sample Input
print(squeeze_cylinders(2, [10, 10]))
print(squeeze_cylinders(2, [4, 12]))
print(squeeze_cylinders(5, [1, 10, 1, 10, 1]))
print(squeeze_cylinders(3, [1, 1, 1]))
print(squeeze_cylinders(2, [5000, 10000]))