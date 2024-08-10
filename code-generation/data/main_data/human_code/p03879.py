# cf16-exhibition-final-openB - Inscribed Bicycle
def main():
    x1, y1, x2, y2, x3, y3 = map(int, open(0).read().split())
    x2 -= x1
    y2 -= y1
    x3 -= x1
    y3 -= y1
    a = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    b = (x3 ** 2 + y3 ** 2) ** 0.5
    c = (x2 ** 2 + y2 ** 2) ** 0.5
    r = abs(x2 * y3 - x3 * y2) / (a + b + c)
    d = max(a, b, c)
    ans = r * d / (2 * r + d)
    print(ans)


if __name__ == "__main__":
    main()
