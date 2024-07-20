def max_nutrition(N, C, sushi):
    total_nutrition = 0
    total_energy = 0
    max_nutrition = 0
    
    for i in range(N):
        total_nutrition += sushi[i][1]
    
    for i in range(N):
        energy = 0
        nutrition = 0
        
        for j in range(N):
            dist = (sushi[j][0] - sushi[i][0] + C) % C
            if dist <= C / 2:
                energy += dist
                nutrition += sushi[j][1]
            else:
                energy += C - dist
                nutrition += sushi[j][1]
        
        if nutrition - energy > max_nutrition:
            max_nutrition = nutrition - energy
    
    return max_nutrition

# Sample Input 1
print(max_nutrition(3, 20, [(2, 80), (9, 120), (16, 1)]))

# Sample Input 2
print(max_nutrition(3, 20, [(2, 80), (9, 1), (16, 120)]))

# Sample Input 3
print(max_nutrition(1, 100000000000000, [(50000000000000, 1)]))

# Sample Input 4
print(max_nutrition(15, 10000000000, [(400000000, 1000000000), (800000000, 1000000000), (1900000000, 1000000000), (2400000000, 1000000000), (2900000000, 1000000000), (3300000000, 1000000000), (3700000000, 1000000000), (3800000000, 1000000000), (4000000000, 1000000000), (4100000000, 1000000000), (5200000000, 1000000000), (6600000000, 1000000000), (8000000000, 1000000000), (9300000000, 1000000000), (9700000000, 1000000000)]))