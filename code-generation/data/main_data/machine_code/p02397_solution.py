def swap_numbers():
    while True:
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        print(min(x, y), max(x, y))

swap_numbers()