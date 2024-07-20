def largest_rectangle_area(matrix):
    def max_area_histogram(row):
        stack = []
        max_area = 0
        index = 0
        while index < len(row):
            if not stack or row[index] >= row[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = row[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
                max_area = max(max_area, area)
        
        while stack:
            top_of_stack = stack.pop()
            area = row[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(max_area, area)
        
        return max_area
    
    max_area = 0
    histogram = [0] * len(matrix[0])
    
    for row in matrix:
        histogram = [h + 1 if cell == '0' else 0 for h, cell in zip(histogram, row)]
        max_area = max(max_area, max_area_histogram(histogram))
    
    return max_area

# Sample Input
matrix = [
    ['0', '0', '1', '0', '0'],
    ['1', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '0'],
    ['0', '0', '0', '1', '0']
]

# Sample Output
largest_rectangle_area(matrix)