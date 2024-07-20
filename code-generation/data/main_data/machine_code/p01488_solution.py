def transfer_train(N, T, AB, routes):
    stations = {}
    for i in range(N):
        a, *info = routes[i]
        for j in range(1, a):
            if info[j-1] not in stations:
                stations[info[j-1]] = {}
            if info[j] not in stations[info[j-1]]:
                stations[info[j-1]][info[j]] = [i, info[j-1], info[j], info[a+j-1]]
            else:
                if info[a+j-1] < stations[info[j-1]][info[j]][3]:
                    stations[info[j-1]][info[j]] = [i, info[j-1], info[j], info[a+j-1]]

    def time_and_transfers(start, end):
        q = [(0, start, 0)]
        visited = set()
        while q:
            time, current, transfers = q.pop(0)
            if current == end:
                return time, transfers
            if current in visited:
                continue
            visited.add(current)
            for s, e, t in stations.get(current, {}).values():
                q.append((time + t, e, transfers + 1 if s != e else transfers))
        return -1

    time, transfers = time_and_transfers(AB[0], AB[1])
    return f"{time} {transfers}"