def remove_stones(N, stones, edges):
    if N == 2:
        return "YES"
    degree = [0] * (N + 1)
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    leaf_count = sum(d == 1 for d in degree)
    if leaf_count == 0:
        return "NO"
    total_stones = sum(stones)
    if total_stones % 2 == 1:
        return "NO"
    return "YES" if leaf_count >= 3 else "NO"