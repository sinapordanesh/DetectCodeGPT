def f_Xi(N, X):
    def popcount(n):
        return bin(n).count('1')
    
    def f(n):
        count = 0
        while n != 0:
            n = n % popcount(n)
            count += 1
        return count
    
    result = []
    for i in range(N):
        Xi = int(X, 2) ^ (1 << (N-1-i))
        result.append(f(Xi))
    
    for res in result:
        print(res)