def max_air_flow():
    import sys
    from math import sqrt

    def area(p):
        return sum(p[i-1][0]*p[i][1]-p[i][0]*p[i-1][1] for i in range(len(p))) / 2

    while True:
        W, N = map(int, input().split())
        if W == 0 and N == 0:
            break

        pillars = []
        for _ in range(N):
            M = int(input())
            p = [tuple(map(int, input().split())) for _ in range(M)]
            pillars.append(p)

        total_area = W * sum(area(p) for p in pillars)
        total_length = sum(sqrt((p[i][0]-p[i-1][0])**2 + (p[i][1]-p[i-1][1])**2) for p in pillars for i in range(len(p)))
        max_air_flow = total_area / total_length
        print(max_air_flow)

max_air_flow()