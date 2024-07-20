def network_mess():
    while True:
        N = int(input())
        if N == 0:
            break
        distances = [list(map(int, input().split())) for _ in range(N)]
        degree = [sum(distance == 1 for distance in row) for row in distances]
        print(*sorted(degree))

network_mess()