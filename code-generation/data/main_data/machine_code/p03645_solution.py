def can_reach_destination(N, M, services):
    for i in range(M):
        if services[i][0] == 1 and services[i][1] == N:
            return "POSSIBLE"
    for i in range(M):
        if services[i][0] == N and services[i][1] == 1:
            return "POSSIBLE"
    return "IMPOSSIBLE"

N, M = map(int, input().split())
services = [list(map(int, input().split())) for _ in range(M)]
print(can_reach_destination(N, M, services))