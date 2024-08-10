a, b = map(int, input().split())

def get_GCD(x, y):
    if x > y:
        x, y = y, x
    y_ = y
    while True:
        if y % x == 0:
            break
        else:
            y += y_
    return y

print(get_GCD(a, b))