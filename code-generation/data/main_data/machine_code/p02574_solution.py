def determine_coprime(N, A):
    pairwise = True
    setwise = True
    gcd_set = A[0]
    
    for i in range(N):
        for j in range(i+1, N):
            if math.gcd(A[i], A[j]) != 1:
                pairwise = False
    
    for num in A:
        gcd_set = math.gcd(gcd_set, num)
    
    if gcd_set != 1:
        setwise = False
    
    if pairwise:
        print("pairwise coprime")
    elif setwise:
        print("setwise coprime")
    else:
        print("not coprime")