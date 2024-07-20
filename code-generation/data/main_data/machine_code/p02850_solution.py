def min_coloring(N, edges):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    colors = [0] * (N-1)
    max_color = 0
    for i in range(1, N+1):
        used_colors = set()
        for neighbor in adj_list[i]:
            if colors[neighbor-2] != 0:
                used_colors.add(colors[neighbor-2])
        for color in range(1, N+1):
            if color not in used_colors:
                colors[i-2] = color
                max_color = max(max_color, color)
                break
    
    print(max_color)
    for color in colors:
        print(color)