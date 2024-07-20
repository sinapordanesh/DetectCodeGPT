def possible_colors(N, A):
    colors = set()
    for size in A:
        colors.add(size)
    return len(colors)