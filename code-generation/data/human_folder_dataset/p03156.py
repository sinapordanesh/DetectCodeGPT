from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    N = int(input())
    A, B = ril()
    P = ril()
    a, b, c = 0, 0, 0
    for p in P:
        if p <= A:
            a += 1
        elif p <= B:
            b += 1
        else:
            c += 1
    print(min(a, b, c))

if __name__ == '__main__':
    main()
