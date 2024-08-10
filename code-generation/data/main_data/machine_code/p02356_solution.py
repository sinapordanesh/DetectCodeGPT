def number_of_windows(N, Q, a, x):
    prefix_sum = [0]
    for i in range(N):
        prefix_sum.append(prefix_sum[-1] + a[i])
        
    for i in range(Q):
        count = 0
        for j in range(N):
            for k in range(j, N):
                if prefix_sum[k+1] - prefix_sum[j] <= x[i]:
                    count += 1
        print(count)