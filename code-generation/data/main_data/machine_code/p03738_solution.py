def compare_magnitudes():
    A, B = map(int, input().split())
    if A > B:
        print("GREATER")
    elif A < B:
        print("LESS")
    else:
        print("EQUAL")

compare_magnitudes()