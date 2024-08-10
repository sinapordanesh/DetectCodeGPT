def cut_the_cake():
    while True:
        n, w, d = map(int, input().split())
        if n == 0 and w == 0 and d == 0:
            break
        cake = [w*d]
        for _ in range(n):
            p, s = map(int, input().split())
            p -= 1
            piece = cake.pop(p)
            x = s % w
            y = s // w
            cake.extend([x*y, piece - x*y])
            cake.sort()
        print(*cake)

cut_the_cake()