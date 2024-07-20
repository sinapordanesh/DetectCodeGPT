def swimming_jam():
    while True:
        n = int(input())
        if n == 0:
            break
        total_time = 0
        for _ in range(n):
            t, c = map(int, input().split())
            total_time += t * c
        print(total_time)

swimming_jam()