def foehn_phenomena():
    N, Q, S, T = map(int, input().split())
    altitudes = [int(input()) for _ in range(N+1)]
    
    temp = 0
    for _ in range(Q):
        L, R, X = map(int, input().split())
        for i in range(L, R+1):
            altitudes[i] += X
        for i in range(N):
            if altitudes[i] < altitudes[i+1]:
                temp -= S * (altitudes[i+1] - altitudes[i])
            else:
                temp += T * (altitudes[i] - altitudes[i+1])
        print(temp)

foehn_phenomena()