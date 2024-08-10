def shifting_matrix(N, L, S):
    A = [[(i-1)*N+j for j in range(1, N+1)] for i in range(1, N+1)]
    
    def shift_left(i):
        nonlocal A
        A[i-1] = A[i-1][-1:] + A[i-1][:-1]
        
    def shift_right(i):
        nonlocal A
        A[i-1] = A[i-1][1:] + A[i-1][:1]
        
    def shift_up(j):
        nonlocal A
        A = [list(x) for x in zip(*A)]
        shift_left(j)
        A = [list(x) for x in zip(*A)]
        
    def shift_down(j):
        nonlocal A
        A = [list(x) for x in zip(*A)]
        shift_right(j)
        A = [list(x) for x in zip(*A)]
        
    i = 0
    while i < L:
        if S[i] == '(':
            start = i
            count = 1
            while count != 0:
                i += 1
                if S[i] == '(':
                    count += 1
                elif S[i] == ')':
                    count -= 1
            end = i
            rep_start = i+1
            while i+1 < L and S[i+1].isdigit():
                i += 1
            rep_end = i+1
            repeat = int(S[rep_start:rep_end])
            for _ in range(repeat):
                shifting_matrix(N, end-start-1, S[start+1:end])
        else:
            shift = S[i]
            i += 1
            num_start = i
            while i < L and S[i].isdigit():
                i += 1
            num_end = i
            num = int(S[num_start:num_end])
            if shift == 'L':
                shift_left(num)
            elif shift == 'R':
                shift_right(num)
            elif shift == 'U':
                shift_up(num)
            elif shift == 'D':
                shift_down(num)
    
    for row in A:
        print(' '.join(map(str, row)))