# A - 1D Matching
def calculate_cables_length(x: int, y: int, total: int) -> tuple:
    MOD = 10 ** 9 + 7
    if y:
        total = (total * y) % MOD
        y -= 1
    else:
        x += 1
    return x, y, total


def main():
    # sort A, B and the lines between A, B shouldn't cross
    # cross <-> not min distance
    N, *AB = map(int, open(0))
    C = [(i, 1) for i in AB[:N]] + [(i, 0) for i in AB[N:]]
    C.sort()
    ans, a, b = 1, 0, 0
    for i, t in C:
        if t:  # laptop
            a, b, ans = calculate_cables_length(a, b, ans)
        else:  # power sources
            b, a, ans = calculate_cables_length(b, a, ans)
    print(ans)


if __name__ == "__main__":
    main()
