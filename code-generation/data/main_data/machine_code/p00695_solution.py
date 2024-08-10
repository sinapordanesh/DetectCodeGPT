def get_largest_rectangle_size(grid):
    def max_histogram_area(heights):
        stack = []
        max_area = 0
        index = 0
        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
        return max_area

    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = int(grid[i][j])

    heights = [0] * len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                heights[j] = 0
            else:
                heights[j] += grid[i][j]

        max_area = max(max_area, max_histogram_area(heights))

    return max_area

m = int(input())
for _ in range(m):
    grid = []
    while True:
        row = input().strip()
        if not row:
            break
        grid.append(row.split())

    print(get_largest_rectangle_size(grid))