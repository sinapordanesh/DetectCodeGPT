def print_row(iterable):
    print(''.join(map(lambda x: str(x).rjust(5), iterable)),
          str(sum(iterable)).rjust(5), sep='')


while True:
    n = int(input())
    if n == 0:
        break

    m = []
    for i in range(n):
        m.append(list(map(int, input().split())))

    last = [0 for i in range(n)]
    for row in m:
        print_row(row)
        for (i, e) in enumerate(row):
            last[i] += e

    print_row(last)