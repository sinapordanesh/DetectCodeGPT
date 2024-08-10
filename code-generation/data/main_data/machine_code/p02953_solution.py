def check_non_decreasing(N, height):
    for i in range(1, N):
        if height[i] < height[i-1]:
            return "No"
    return "Yes" 

# Sample Input 1
N = 5
height = [1, 2, 1, 1, 3]
print(check_non_decreasing(N, height))

# Sample Input 2
N = 4
height = [1, 3, 2, 1]
print(check_non_decreasing(N, height))

# Sample Input 3
N = 5
height = [1, 2, 3, 4, 5]
print(check_non_decreasing(N, height))

# Sample Input 4
N = 1
height = [1000000000]
print(check_non_decreasing(N, height))