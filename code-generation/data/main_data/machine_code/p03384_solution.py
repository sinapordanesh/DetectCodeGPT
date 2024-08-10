def favorite_tree(n, edges):
    favorite_tree = [-1] * n
    stack = []
    for i in range(1, n):
        if favorite_tree[edges[i-1][0] - 1] == -1:
            stack.append(edges[i-1][0])
        else:
            current = stack[-1]
            while favorite_tree[current - 1] != -1 and favorite_tree[current - 1] < edges[i-1][1]:
                stack.pop()
                if not stack:
                    return -1
                current = stack[-1]
            favorite_tree[edges[i-1][1] - 1] = stack[-1]
    return ' '.join(map(str, favorite_tree))

n = 6
edges = [(1, 2), (1, 3), (1, 4), (1, 5), (5, 6)]
print(favorite_tree(n, edges))