def count_pairs():
    while True:
        L = int(input())
        if L == 0:
            break
        count = 0
        for a in range(1, int(L ** 0.5) + 1):
            if L % a == 0:
                b = L // a
                if b >= a:
                    count += 1
                    if a != b:
                        count += 1
        print(count)

count_pairs()