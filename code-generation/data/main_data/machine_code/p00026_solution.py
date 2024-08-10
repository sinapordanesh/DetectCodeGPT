def dropping_ink(input_list):
    paper = [[0 for _ in range(10)] for _ in range(10)]
    total_cells = 100
    max_density = 0
    
    for point in input_list:
        x, y, size = map(int, point.split(','))
        paper[y][x] += 1
        
        if size == 1:  # Small
            for i in range(max(0, y-1), min(10, y+2)):
                for j in range(max(0, x-1), min(10, x+2)):
                    paper[i][j] += 1
        elif size == 2:  # Medium
            for i in range(max(0, y-2), min(10, y+3)):
                for j in range(max(0, x-2), min(10, x+3)):
                    paper[i][j] += 1
        elif size == 3:  # Large
            for i in range(max(0, y-3), min(10, y+4)):
                for j in range(max(0, x-3), min(10, x+4)):
                    paper[i][j] += 1
    
    count_zeros = sum(row.count(0) for row in paper)
    max_density = max(max(row) for row in paper)
    
    return count_zeros, max_density

# Sample Input
input_list = ["2,5,3", "3,6,1", "3,4,2", "4,5,2", "3,6,3", "2,4,1"]
result = dropping_ink(input_list)
print(result[0])
print(result[1])