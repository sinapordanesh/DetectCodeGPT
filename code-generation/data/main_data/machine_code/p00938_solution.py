def wall_clocks(n, w, d, members):
    count = 0
    for i in range(n):
        x, y, f = members[i]
        if f == 'N' or f == 'S':
            view_left = max(x-45, 0)
            view_right = min(x+45, w)
        else:
            view_left = max(y-45, 0)
            view_right = min(y+45, d)
        
        count += all((view_left <= px <= view_right) for px, py, pf in members if f == pf)
    
    return count

# Sample Input
print(wall_clocks(2, 10, 6, [(4, 4, 'E'), (6, 4, 'W')])) # 2
print(wall_clocks(2, 10, 6, [(2, 4, 'E'), (6, 4, 'W')])) # 1
print(wall_clocks(2, 10, 6, [(3, 2, 'S'), (6, 4, 'W')])) # 1
print(wall_clocks(6, 10, 6, [(1, 5, 'N'), (7, 1, 'N'), (8, 2, 'E'), (9, 1, 'S'), (4, 4, 'S'), (3, 3, 'W')])) # 3
print(wall_clocks(4, 10, 6, [(4, 3, 'W'), (2, 4, 'N'), (4, 4, 'W'), (3, 3, 'S')])) # 2
print(wall_clocks(4, 100000, 40000, [(25000, 25000, 'S'), (20000, 30000, 'S'), (75000, 25000, 'S'), (80000, 30000, 'S')])) # 1