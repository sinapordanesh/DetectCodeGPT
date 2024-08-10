def calculate_sum(T, testcases):
    for i in range(T):
        N, M, A, B = testcases[i]
        total_sum = 0
        for i in range(N):
            total_sum += (A * i + B) // M
        print(total_sum)