def compute_sum():
    while True:
        try:
            a, b = map(int, input().split())
            print(a + b)
        except:
            break

compute_sum()