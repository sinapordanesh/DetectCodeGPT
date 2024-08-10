def place_flags(N, D, coordinates):
    coordinates.sort(key=lambda x: x[0])
    result = []
    for i in range(N):
        result.append(coordinates[i][0])
    if all(result[i] - result[i-1] >= D for i in range(1, N)):
        print("Yes")
        for value in result:
            print(value)
    else:
        print("No")