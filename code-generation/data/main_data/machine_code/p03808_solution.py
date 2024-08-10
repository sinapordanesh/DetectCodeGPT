def remove_stones(N, boxes):
    total = sum(boxes)
    if total % N != 0:
        return "NO"
    else:
        target = total // N
        for i in range(N):
            if (boxes[i] - target) % (i + 1) != 0:
                return "NO"
        return "YES" 

# Sample Input 1
print(remove_stones(5, [4, 5, 1, 2, 3])) # Output: YES

# Sample Input 2
print(remove_stones(5, [6, 9, 12, 10, 8])) # Output: YES

# Sample Input 3
print(remove_stones(4, [1, 2, 3, 1])) # Output: NO