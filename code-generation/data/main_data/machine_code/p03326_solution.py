def max_total_value_of_cakes(N, M, cakes):
    from itertools import combinations
    
    max_value = 0
    
    for i in range(1, M+1):
        for cake_combination in combinations(cakes, i):
            total_beauty = sum([cake[0] for cake in cake_combination])
            total_tastiness = sum([cake[1] for cake in cake_combination])
            total_popularity = sum([cake[2] for cake in cake_combination])
            
            max_value = max(max_value, abs(total_beauty) + abs(total_tastiness) + abs(total_popularity))
    
    return max_value

# Input
N, M = map(int, input().split())
cakes = [list(map(int, input().split())) for _ in range(N)]

# Output
print(max_total_value_of_cakes(N, M, cakes))