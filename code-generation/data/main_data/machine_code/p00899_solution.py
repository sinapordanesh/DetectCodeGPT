def shortest_possible_name():
    while True:
        n = int(input())
        if n == 0:
            break
        cities = [input() for _ in range(n)]
        shortest_name = cities[0]
        for i in range(1, n):
            for j in range(len(cities[i])):
                if cities[i][j:] in shortest_name:
                    shortest_name += cities[i][j+len(shortest_name):]
                    break
            else:
                shortest_name += cities[i]
        print(len(shortest_name))

shortest_possible_name()