def next_mayor():
    while True:
        n, p = map(int, input().split())
        if n == 0 and p == 0:
            break
        
        winner = (p - 1) % n
        print(winner)

next_mayor()