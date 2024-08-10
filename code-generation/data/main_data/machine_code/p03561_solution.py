def find_sequence(K, N):
    X = K**N
    result = []
    count = 0
    
    for i in range(1, K+1):
        result.append(i)
        count += 1
        if count == (X//2):
            break
            
    return result * N

K, N = map(int, input().split())
print(*find_sequence(K, N))