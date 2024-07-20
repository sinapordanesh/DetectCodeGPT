def city_id_numbers(N, M, cities):
    cities.sort(key=lambda x: x[1])
    city_id = []
    for i in range(M):
        city_id.append(str(cities[i][0]).zfill(6) + str(i+1).zfill(6))
    return city_id

#Sample Input
N = 2
M = 3
cities = [(1, 32), (2, 63), (1, 12)]

print(*city_id_numbers(N, M, cities), sep='\n')