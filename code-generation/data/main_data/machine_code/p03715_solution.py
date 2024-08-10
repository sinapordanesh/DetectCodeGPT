def min_chocolate_difference(H, W):
    area = H * W
    if area % 3 == 0:
        return 0
    min_diff = min(abs(area // 3 - area // 3 * 2), abs(area // 3 * 2 - area // 3))
    return min_diff

# Test the function
print(min_chocolate_difference(3, 5)) # 0
print(min_chocolate_difference(4, 5)) # 2
print(min_chocolate_difference(5, 5)) # 4
print(min_chocolate_difference(100000, 2)) # 1
print(min_chocolate_difference(100000, 100000)) # 50000