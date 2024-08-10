def minimum_bombs_needed(N, D, A, monsters):
    monsters.sort()
    bombs_needed = 0
    healths = [0] * (N+1)
    
    for i in range(N):
        x, h = monsters[i]
        healths[i+1] = healths[i]
        
        if healths[i] < h:
            diff = h - healths[i]
            bombs = (diff + A - 1) // A
            bombs_needed += bombs
            healths[i+1] += bombs * A
            healths[i+1] = min(healths[i+1], h)
            
            right = x + 2*D
            idx = bisect_right(monsters, (right, float('inf')))
            healths[idx] -= bombs * A
    
    return bombs_needed

# Input
N, D, A = 3, 3, 2
monsters = [(1, 2), (5, 4), (9, 2)]

print(minimum_bombs_needed(N, D, A, monsters))

N, D, A = 9, 4, 1
monsters = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 2), (7, 3), (8, 4), (9, 5)]

print(minimum_bombs_needed(N, D, A, monsters))

N, D, A = 3, 0, 1
monsters = [(300000000, 1000000000), (100000000, 1000000000), (200000000, 1000000000)]

print(minimum_bombs_needed(N, D, A, monsters))