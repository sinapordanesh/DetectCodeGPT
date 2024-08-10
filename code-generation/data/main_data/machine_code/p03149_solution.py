def arrange_into_1974():
    N1, N2, N3, N4 = map(int, input().split())
    if sorted([N1, N2, N3, N4]) == [1, 4, 7, 9]:
        print("YES")
    else:
        print("NO")

arrange_into_1974()