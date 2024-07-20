def generate_substance(N, M_a, M_b, chemicals):
    from itertools import combinations
    
    min_cost = float('inf')
    
    for i in range(1, N+1):
        for combination in combinations(chemicals, i):
            total_A = sum([chem[0] for chem in combination])
            total_B = sum([chem[1] for chem in combination])
            total_cost = sum([chem[2] for chem in combination])
            
            if total_A == M_a and total_B == M_b:
                min_cost = min(min_cost, total_cost)
    
    if min_cost == float('inf'):
        return -1
    else:
        return min_cost

# Sample Input 1
N = 3
M_a = 1
M_b = 1
chemicals = [(1, 2, 1), (2, 1, 2), (3, 3, 10)]
print(generate_substance(N, M_a, M_b, chemicals))

# Sample Input 2
N = 1
M_a = 1
M_b = 10
chemicals = [(10, 10, 10)]
print(generate_substance(N, M_a, M_b, chemicals))