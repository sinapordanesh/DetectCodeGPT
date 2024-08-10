def sugar_water(A, B, C, D, E, F):
    max_sugar_water = 0
    max_sugar = 0
    
    for a in range(F // 100 + 1):
        for b in range(F - 100 * a + 1):
            if a == 0 and b == 0:
                continue
            if a * A + b * B > E * (a * A + b * B) // 100:
                continue
            if C * b <= E * a and D * b >= E * a:
                if 100 * (b + a) <= F:
                    sugar_water = 100 * (b + a)
                    if max_sugar_water * (max_sugar + b) < sugar_water * (max_sugar + a):
                        max_sugar_water = sugar_water
                        max_sugar = a
    
    return max_sugar_water, max_sugar

# Sample Input 1
print(sugar_water(1, 2, 10, 20, 15, 200))

# Sample Input 2
print(sugar_water(1, 2, 1, 2, 100, 1000))

# Sample Input 3
print(sugar_water(17, 19, 22, 26, 55, 2802))