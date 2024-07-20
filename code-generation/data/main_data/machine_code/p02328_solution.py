def largest_rectangle_area(N, heights):
    stack = []
    max_area = 0
    i = 0
    while i < N:
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = heights[top] * (i if not stack else i - stack[-1] - 1)
            max_area = max(max_area, area)
    
    while stack:
        top = stack.pop()
        area = heights[top] * (i if not stack else i - stack[-1] - 1)
        max_area = max(max_area, area)
    
    return max_area

# Input
N = 8
heights = [2, 1, 3, 5, 3, 4, 2, 1]

# Output
print(largest_rectangle_area(N, heights))

# Input
N = 3
heights = [2, 0, 1]

# Output
print(largest_rectangle_area(N, heights))