def can_make_all_strings(N, M, s, edges):
    def dfs(node, target_letter):
        if visited[node] != "":
            return visited[node] == target_letter
        visited[node] = target_letter
        for neighbor in graph[node]:
            if not dfs(neighbor, "A" if target_letter == "B" else "B"):
                return False
        return True

    graph = {i: [] for i in range(1, N + 1)}
    visited = {i: "" for i in range(1, N + 1)}

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        if visited[i] == "":
            if not dfs(i, s[i-1]):
                return "No"
    
    return "Yes"

# Sample Input 1
print(can_make_all_strings(2, 3, "AB", [(1, 1), (1, 2), (2, 2)]))

# Sample Input 2
print(can_make_all_strings(4, 3, "ABAB", [(1, 2), (2, 3), (3, 1)]))

# Sample Input 3
print(can_make_all_strings(13, 23, "ABAAAABBBBAAB", [(7, 1), (10, 6), (1, 11), (2, 10), (2, 8), (2, 11), (11, 12), (8, 3), (7, 12), (11, 2), (13, 13), (11, 9), (4, 1), (9, 7), (9, 6), (8, 13), (8, 6), (4, 10), (8, 7), (4, 3), (2, 1), (8, 12), (6, 9)]))

# Sample Input 4
print(can_make_all_strings(13, 17, "BBABBBAABABBA", [(7, 1), (7, 9), (11, 12), (3, 9), (11, 9), (2, 1), (11, 5), (12, 11), (10, 8), (1, 11), (1, 8), (7, 7), (9, 10), (8, 8), (8, 12), (6, 2), (13, 11)]))