def save_cats(N, M, piles, fences):
    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
    
    total_length = sum(distance(piles[f[0] - 1], piles[f[1] - 1]) for f in fences)
    return '{:.3f}'.format(total_length)

print(save_cats(3, 3, [(0, 0), (3, 0), (0, 4)], [(1, 2), (2, 3), (3, 1)]))
print(save_cats(4, 3, [(0, 0), (-100, 0), (100, 0), (0, 100)], [(1, 2), (1, 3), (1, 4)]))
print(save_cats(6, 7, [(2, 0), (6, 0), (8, 2), (6, 3), (0, 5), (1, 7)], [(1, 2), (2, 3), (3, 4), (4, 1), (5, 1), (5, 4), (5, 6)]))
print(save_cats(6, 6, [(0, 0), (0, 1), (1, 0), (30, 0), (0, 40), (30, 40)], [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]))