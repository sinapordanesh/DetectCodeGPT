def biscuits_production():
    A, B, T = map(int, input().split())
    total_biscuits = 0
    time = A
    while time <= T + 0.5:
        total_biscuits += B
        time += A
    print(total_biscuits)

biscuits_production()