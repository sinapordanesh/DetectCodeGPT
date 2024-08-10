def inner_product(v1, v2):
    return v1.real * v2.real + v1.imag * v2.imag


# ????????????b???????????????a??????????????´????????£?°???±???????????????????????????
def projection(a, b):
    return a * inner_product(a, b) / (abs(a) ** 2)


def solve(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    pro = projection(a, b)
    t = p0 + pro
    return t


def main():
    x_p0, y_p0, x_p1, y_p1 = map(float, input().split())
    p0 = complex(x_p0, y_p0)
    p1 = complex(x_p1, y_p1)
    q = int(input())
    for _ in range(q):
        p2 = complex(*map(float, input().split()))
        t = solve(p0, p1, p2)
        print("{:.10f} {:.10f}".format(t.real, t.imag))


if __name__ == '__main__':
    main()
