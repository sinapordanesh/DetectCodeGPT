def adjacency_list_to_matrix(n, adjacency_list):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        if len(adjacency_list[i]) > 1:
            for j in range(1, len(adjacency_list[i])):
                matrix[i][adjacency_list[i][j] - 1] = 1
    return matrix

n = int(input())
adjacency_list = [[] for _ in range(n)]
for i in range(n):
    adjacency_list[i] = list(map(int, input().split()))    

result = adjacency_list_to_matrix(n, adjacency_list)
for row in result:
    print(' '.join(map(str, row)))