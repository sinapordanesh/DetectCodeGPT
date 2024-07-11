def main():
    import numpy as np
    n = int(input())
    a = np.full((n, n), ".", dtype=str)
    a3 = np.array([[".", "a", "a"], ["b", ".", "."], ["b", ".", "."]], dtype=str)
    a4 = np.array([["a", "a", "b", "c"], ["d", "d", "b", "c"],
                   ["a", "c", "d", "d"], ["a", "c", "b", "b"]], dtype=str)
    a5 = np.array([["c", "c", "d", "d", "e"],
                   ["j", ".", "a", "a", "e"],
                   ["j", "b", ".", ".", "f"],
                   ["i", "b", ".", ".", "f"],
                   ["i", "h", "h", "g", "g"]], dtype=str)
    a7 = np.array([[".", "c", "c", "d", "d", "c", "c"],
                   ["c", ".", "a", "a", ".", "a", "a"],
                   ["c", "b", ".", ".", "b", ".", "."],
                   ["d", "b", ".", ".", "b", ".", "."],
                   ["d", ".", "a", "a", ".", "a", "a"],
                   ["c", "b", ".", ".", "b", ".", "."],
                   ["c", "b", ".", ".", "b", ".", "."]], dtype=str)
    a6 = np.full((6, 6), ".", dtype=str)
    for i in range(2):
        a6[3*i:3*i+3, 3*i:3*i+3] = a3
    a11 = np.full((11, 11), ".", dtype=str)
    a11[:4, :4] = a4
    a11[4:, 4:] = a7

    if n == 2:
        print(-1)
        return
    elif n == 3:
        a = a3
    elif n == 6:
        a = a6
    elif n == 7:
        a = a7
    elif n == 11:
        a = a11
    else:
        for p in range(n):
            q = n-4*p
            if q % 5 == 0:
                q //= 5
                break
        for i in range(p):
            a[4*i:4*i+4, 4*i:4*i+4] = a4
        p = 4*p
        for i in range(q):
            a[p+5*i:p+5*i+5, p+5*i:p+5*i+5] = a5

    a = a.tolist()
    for i in a:
        print("".join(i))


main()
