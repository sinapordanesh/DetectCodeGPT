def construct_matrix(H, W, h, w):
    if h == 1 and w == 1:
        return "No"
    
    total_sum = H * W
    subrectangle_sum = h * w
    remainder_sum = total_sum - subrectangle_sum
    
    if remainder_sum <= 0:
        return "No"
    
    matrix = [[1 for j in range(W)] for i in range(H)]
    
    for i in range(0, H, h):
        for j in range(0, W, w):
            for a in range(i, i + h):
                for b in range(j, j + w):
                    matrix[a][b] = -1
    
    matrix[0][0] = remainder_sum
    
    return "Yes\n" + "\n".join([" ".join(str(x) for x in row) for row in matrix])


# Example Usage
print(construct_matrix(3, 3, 2, 2))
print(construct_matrix(2, 4, 1, 2))
print(construct_matrix(3, 4, 2, 3))