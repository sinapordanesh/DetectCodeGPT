def minimum_total_stool_height(N, heights):
    total = 0
    max_height = 0
    for height in heights[::-1]:
        if height > max_height:
            max_height = height
        else:
            total += max_height - height + 1
            max_height += 1
    return total

# Input processing
N = int(input())
heights = list(map(int, input().split()))

# Function Call
print(minimum_total_stool_height(N, heights))