def water_tank_schedule():
    while True:
        N, L = map(int, input().split())
        if N == 0 and L == 0:
            break
        total_water = 0
        for i in range(N):
            s, t, u = map(int, input().split())
            total_water += u * (t - s)
        print("{:.6f}".format(L / total_water))

water_tank_schedule()