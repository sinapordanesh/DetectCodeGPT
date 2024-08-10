def sugar_water(A, B, C, D, E, F):
    max_water_mass = 0
    max_sugar_mass = 0
    
    for a in range(F // (100 * A) + 1):
        for b in range((F - 100 * A * a) // (100 * B) + 1):
            if a == 0 and b == 0:
                continue
            if 100 * (E * b) <= (A * a):
                water_mass = 100 * (a * A + b * B)
                if water_mass <= F:
                    if (max_sugar_mass == 0) or ((100 * b * E * max_water_mass) > (max_sugar_mass * water_mass)):
                        max_water_mass = water_mass
                        max_sugar_mass = 100 * b * E

    return f"{max_water_mass} {max_sugar_mass}"