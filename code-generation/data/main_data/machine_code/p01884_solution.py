def find_pairs(n, edges):
    subtree_count = [0] * (n + 1)
    result = 0
    
    def dfs(node, parent):
        nonlocal result
        subtree_count[node] = 1
        for child in edges[node]:
            if child != parent:
                dfs(child, node)
                subtree_count[node] += subtree_count[child]
        
        result += subtree_count[node] * (n - subtree_count[node])
    
    dfs(1, 0)
    
    return result // 2

# Sample Input 1
print(find_pairs(5, {1: [2, 3, 4, 5], 2: [1], 3: [1], 4: [1], 5: [1]}))

# Sample Input 2
print(find_pairs(6, {1: [2, 5], 2: [1, 3], 3: [2, 4], 4: [3], 5: [1, 6], 6: [5]}))

# Sample Input 3
print(find_pairs(13, {1: [2, 3], 2: [1, 4, 5], 3: [1, 6, 7], 4: [2, 8, 9], 5: [2], 6: [3, 10], 7: [3, 11], 8: [4, 12], 9: [4], 10: [6], 11: [7, 13], 12: [8], 13: [11]}))