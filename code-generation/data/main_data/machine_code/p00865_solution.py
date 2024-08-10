def expected_allowance():
    while True:
        n, m, k = map(int, input().split())
        if n == 0 and m == 0 and k == 0:
            break
        
        total = 0
        for i in range(1, m + 1):
            total += i
        
        expected = 0
        for i in range(1, m + 1):
            expected += (i / total) * max(1, i - k)
        
        print(f'{expected:.8f}')

expected_allowance()