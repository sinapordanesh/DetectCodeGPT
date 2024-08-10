def fastest_finger_fast(N, K, Q, A):
    scores = [K] * N
    
    for i in range(Q):
        scores[A[i]-1] += 1
        for j in range(N):
            if A[i] != j+1:
                scores[j] -= 1
    
    result = []
    for score in scores:
        if score > 0:
            result.append("Yes")
        else:
            result.append("No")
    
    return result