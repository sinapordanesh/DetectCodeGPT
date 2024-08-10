from itertools import permutations

def count_octahedra(colors):
    unique_colors = set(colors)
    if len(unique_colors) == 1:
        return 1
    return len(set(permutations(unique_colors)))

while True:
    try:
        colors = input().strip().split()
        print(count_octahedra(colors))
    except EOFError:
        break