def game_rounds(T, test_cases):
    for case in test_cases:
        N = case[0]
        A = case[1:N+1]
        S = case[N+1]

        x = 0
        for i in range(N):
            if S[i] == '1':
                x = x ^ A[i]

        if x == 0:
            print(0)
        else:
            print(1)