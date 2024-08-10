def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    k = N.bit_length()

    if 1<<(k-1) == N:
        print('No')
        exit()
    print('Yes')
    if N == 3:
        for i in range(1, 6):
            print(i, i+1)
        exit()

    N0 = 1<<(k-1)
    e = [(N0-1, N+1)]
    for i in range(1, N0-1):
        e.append((i, i+1))
        e.append((i+N, i+1+N))

    if N%2 == 0:
        v = N ^ N0
        e.append((N, v))
        e.append((N*2, N0))
        for i in range(N0, N):
            if i % 2 == 0:
                e.append((i, v))
                e.append((i + N, i+N+1))
            else:
                e.append((i, i - 1))
                e.append((i + N, v + 1))
    else:
        for i in range(N0, N + 1):
            if i % 2 == 0:
                e.append((i, 2))
                e.append((i + N, i + 1 + N))
            else:
                e.append((i, i - 1))
                e.append((i + N, 3 + N))
    for edge in e:
        print(*edge)


if __name__ == '__main__':
    main()
