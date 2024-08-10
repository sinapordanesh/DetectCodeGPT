def see_ocean(N, heights):
    count = 1
    max_height = heights[0]
    for i in range(1, N):
        if heights[i] >= max_height:
            count += 1
            max_height = heights[i]
    return count

N = 4
heights = [6, 5, 6, 8]
print(see_ocean(N, heights))

N = 5
heights = [4, 5, 3, 5, 4]
print(see_ocean(N, heights))

N = 5
heights = [9, 5, 6, 8, 4]
print(see_ocean(N, heights))