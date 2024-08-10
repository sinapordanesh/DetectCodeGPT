def grade(m, f, r):
    if m == -1 or f == -1:
        return 'F'

    if 80 <= m+f:
        return 'A'

    if 65 <= m+f:
        return 'B'

    if 50 <= m+f:
        return 'C'

    if 30 <= m+f:
        return 'C' if 50 <= r else 'D'

    return 'F'

def main():
    while True:
        m, f, r = [int(x) for x in input().split()]
        if m == f == r == -1:
            break

        print(grade(m,f,r))

if __name__ == '__main__':
    main()

