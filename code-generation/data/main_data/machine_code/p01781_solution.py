def cube_coloring(X, Y, Z, A, B, C, N):
    result = [0] * N
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                distance = abs(x - A) + abs(y - B) + abs(z - C)
                color = (distance % N) + 1
                result[color - 1] += 1
    return result

# Test the function
print(cube_coloring(2, 2, 2, 0, 0, 0, 5))
print(cube_coloring(4, 3, 3, 1, 1, 1, 3))
print(cube_coloring(2000, 2000, 2000, 1000, 1000, 1000, 1))