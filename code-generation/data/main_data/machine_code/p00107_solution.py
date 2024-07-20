def carry_cheese():
    while True:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break
        n = int(input())
        for _ in range(n):
            r = int(input())
            if (a**2 + b**2) <= r**2 or (a**2 + c**2) <= r**2 or (b**2 + c**2) <= r**2:
                print("NA")
            else:
                print("OK")

carry_cheese()