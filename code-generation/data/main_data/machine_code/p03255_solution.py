def min_energy(N, X, positions):
    min_energy = 0
    
    k = 0
    for i in range(N):
        energy = (positions[i] * (positions[i] + 1) * (2 * positions[i] + 1)) // 6
        min_energy += (positions[i] - k) * (X + k * (k + 1))
        k += 1
    
    return min_energy

# Sample Input 1
print(min_energy(2, 100, [1, 10]))

# Sample Input 2
print(min_energy(5, 1, [1, 999999997, 999999998, 999999999, 1000000000])) 

# Sample Input 3
print(min_energy(10, 8851025, [38, 87, 668, 3175, 22601, 65499, 90236, 790604, 4290609, 4894746]))

# Sample Input 4
print(min_energy(16, 10, [1, 7, 12, 27, 52, 75, 731, 13856, 395504, 534840, 1276551, 2356789, 9384806, 19108104, 82684732, 535447408]))