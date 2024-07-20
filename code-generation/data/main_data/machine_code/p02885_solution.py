def uncovered_parts_length():
    A, B = map(int, input().split())
    if A >= B * 2:
        print(0)
    else:
        print(B * 2 - A)

uncovered_parts_length()