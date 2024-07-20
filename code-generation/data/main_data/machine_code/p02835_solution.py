def check_bust_or_win():
    A = list(map(int, input().split()))
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")