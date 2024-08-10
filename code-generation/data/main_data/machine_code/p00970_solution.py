def emergency_evacuation(r, s, p, passengers):
    steps = 0
    while len(passengers) > 0:
        empty_seats = [[0] * (2 * s) for _ in range(r)]
        for i, j in passengers:
            empty_seats[i-1][j-1] = 1
        new_passengers = []
        for i, j in passengers:
            if j > 1 and empty_seats[i-1][j-2] == 0:
                new_passengers.append((i, j-1))
                empty_seats[i-1][j-2] = 1
            elif j < 2 * s and empty_seats[i-1][j] == 0:
                new_passengers.append((i, j+1))
                empty_seats[i-1][j] = 1
            elif i < r and empty_seats[i][j-1] == 0:
                new_passengers.append((i+1, j))
                empty_seats[i][j-1] = 1
        passengers = new_passengers
        steps += 1
    return steps

# Sample input
print(emergency_evacuation(5, 2, 7, [(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (4, 4), (5, 2)]))
print(emergency_evacuation(500, 500, 16, [(1, 1), (1, 2), (1, 999), (1, 1000), (2, 1), (2, 2), (2, 999), (2, 1000), (3, 1), (3, 2), (3, 999), (3, 1000), (499, 500), (499, 501), (499, 999), (499, 1000)]))