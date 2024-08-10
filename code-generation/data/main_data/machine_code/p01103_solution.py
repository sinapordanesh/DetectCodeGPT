def calculate_pond_capacity(depth, width, garden_map):
    def is_valid_pond(i, j, pond_height):
        for x in range(i, i + depth):
            for y in range(j, j + width):
                if x == i or x == i + depth - 1 or y == j or y == j + width - 1:
                    if garden_map[x][y] >= pond_height:
                        return False
                else:
                    if garden_map[x][y] <= pond_height:
                        return False
        return True
    
    max_capacity = 0
    for i in range(1, len(garden_map) - depth):
        for j in range(1, len(garden_map[0]) - width):
            pond_height = min([garden_map[x][y] for x in range(i, i + depth) for y in range(j, j + width)])
            if is_valid_pond(i, j, pond_height):
                capacity = sum([pond_height - garden_map[x][y] for x in range(i, i + depth) for y in range(j, j + width)])
                max_capacity = max(max_capacity, capacity)
    
    return max_capacity