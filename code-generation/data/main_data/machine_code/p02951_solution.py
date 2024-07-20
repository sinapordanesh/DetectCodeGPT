def remaining_water():
    A, B, C = map(int, input().split())
    transfer = min(C, A-B)
    print(C-transfer)

remaining_water()