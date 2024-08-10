def find_sequences(N, M, A):
    if sum(A) != N:
        print("Impossible")
        return
    
    a = A.copy()
    b = A[::-1]
    
    print(" ".join(map(str, a)))
    print(M)
    print(" ".join(map(str, b)) if M > 1 else b[0])