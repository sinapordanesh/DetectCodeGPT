import numpy as np
import sys

def min_spanning_tree(n, adj_matrix):
    total_weight = 0
    visited = [False] * n
    key = [sys.maxsize] * n
    key[0] = 0
    
    for _ in range(n):
        min_key = sys.maxsize
        min_index = -1
        
        for i in range(n):
            if not visited[i] and key[i] < min_key:
                min_key = key[i]
                min_index = i
        
        visited[min_index] = True
        total_weight += min_key
        
        for i in range(n):
            if adj_matrix[min_index][i] != -1 and not visited[i] and adj_matrix[min_index][i] < key[i]:
                key[i] = adj_matrix[min_index][i]
    
    return total_weight

# Sample Input
n = 5
adj_matrix = np.array([[-1, 2, 3, 1, -1],
                        [2, -1, -1, 4, -1],
                        [3, -1, -1, 1, 1],
                        [1, 4, 1, -1, 3],
                        [-1, -1, 1, 3, -1]])

print(min_spanning_tree(n, adj_matrix))