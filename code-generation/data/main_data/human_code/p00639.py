from sys import stdin

def solve():
    file_input = stdin
    while True:
        D = float(file_input.readline())
        if D == 0:
            break
        px, py, vx, vy = map(float, file_input.readline().split())
        if px * vy - py * vx == 0:
            OP = (px ** 2 + py ** 2) ** 0.5
            if px * vx + py * vy < 0:
                if OP <= D:
                    print(OP)
                else:
                    print('impossible')
            else:
                d = 2 - OP
                if d <= D:
                    print(d)
                else:
                    print('impossible')
        else:
            print('impossible')

solve()
