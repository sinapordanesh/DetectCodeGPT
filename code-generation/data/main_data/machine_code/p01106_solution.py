def folding_ribbon(n, i, j):
    sequence = ''
    for _ in range(n):
        if i > 2**(n-1):
            sequence += 'R'
            i = 2**n - i
        else:
            sequence += 'L'
        i = (i + 1) // 2 if i % 2 == 1 else i // 2
    return sequence

n, i, j = map(int, input().split())
while n != 0:
    print(folding_ribbon(n, i, j))
    n, i, j = map(int, input().split())