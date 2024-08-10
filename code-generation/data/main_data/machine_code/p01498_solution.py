def king_slime(N, W, H, slimes):
    def find_parent(parent, i):
        if parent[i] == i:
            return i
        return find_parent(parent, parent[i])
    
    def union(parent, rank, x, y):
        x_root = find_parent(parent, x)
        y_root = find_parent(parent, y)
        
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    
    def moves_to_unite(slimes):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        parent = [i for i in range(len(slimes))]
        rank = [0] * len(slimes)
        moves = 0
        
        while len(set(parent)) > 1:
            moves += 1
            for i in range(len(slimes)):
                x, y = slimes[i]
                for dx, dy in directions:
                    new_x, new_y = x+dx, y+dy
                    if (new_x, new_y) in slimes:
                        union(parent, rank, i, slimes.index((new_x, new_y)))
                    elif new_x < 1 or new_x > W or new_y < 1 or new_y > H:
                        union(parent, rank, i, len(slimes))
        
        return moves
    
    return moves_to_unite(slimes)

print(king_slime(4, 3, 3, [(1,1), (1,3), (3,1), (3,3)]))
print(king_slime(2, 3, 3, [(2,2), (3,3)]))
print(king_slime(2, 4, 4, [(2,2), (3,3)]))
print(king_slime(2, 4, 4, [(2,2), (2,3)]))