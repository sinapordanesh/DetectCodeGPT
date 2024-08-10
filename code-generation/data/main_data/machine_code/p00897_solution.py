def long_distance_taxi():
    while True:
        N, M, cap = map(int, input().split())
        if N == 0 and M == 0 and cap == 0:
            break
        src, dest = input().split()
        cities = {}
        for i in range(N):
            c1, c2, d = input().split()
            d = int(d)
            if c1 not in cities:
                cities[c1] = []
            if c2 not in cities:
                cities[c2] = []
            cities[c1].append((c2, d))
            cities[c2].append((c1, d))
        lpg_stations = []
        for i in range(M):
            lpg_station = input()
            lpg_stations.append(lpg_station)
        queue = [(src, 0, cap)]
        visited = set()
        visited.add((src, cap))
        while queue:
            current_city, distance, fuel = queue.pop(0)
            if current_city == dest:
                print(distance)
                break
            if fuel == 0:
                continue
            for neighbor, dist in cities[current_city]:
                if fuel >= dist and (neighbor, fuel - dist) not in visited:
                    queue.append((neighbor, distance + dist, fuel - dist))
                    visited.add((neighbor, fuel - dist))
            if current_city in lpg_stations and (current_city, cap) not in visited:
                queue.append((current_city, distance, cap))
                visited.add((current_city, cap))
        else:
            print(-1)

long_distance_taxi()