def find_max_f():
    N = int(input())
    a = list(map(int, input().split()))
    max_f = 0

    for m in range(1, 10**5+1):
        f_m = sum([m % x for x in a])
        max_f = max(max_f, f_m)

    print(max_f)

find_max_f()