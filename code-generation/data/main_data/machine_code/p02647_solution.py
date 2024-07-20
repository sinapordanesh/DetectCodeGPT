def bulb_intensity(N, K, A):
    for _ in range(K):
        new_intensity = [0] * N
        for i in range(N):
            left = max(0, i - A[i])
            right = min(N-1, i + A[i])
            new_intensity[left] += 1
            if right+1 < N:
                new_intensity[right+1] -= 1
        
        for i in range(1, N):
            new_intensity[i] += new_intensity[i-1]
        
        A = new_intensity
    
    return A