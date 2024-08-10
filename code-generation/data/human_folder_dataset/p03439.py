def apc001_c():
    import sys
    n = int(input())

    def ask(x:int):
        print(x)
        sys.stdout.flush()
        res = str(input())
        return res

    lower = 0
    seat_low = ask(lower)
    if seat_low == 'Vacant': return

    upper = n-1
    seat_up = ask(upper)
    if seat_up == 'Vacant': return

    while upper - lower > 1:
        x = (upper + lower) // 2
        s = ask(x)
        if s == 'Vacant': return
        if x % 2 == 0:
            if s == seat_low: lower = x
            else: upper = x
        else:
            if s == seat_up: lower = x
            else: upper = x

if __name__ == '__main__':
    apc001_c()