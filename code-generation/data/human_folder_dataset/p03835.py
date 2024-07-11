K, S = list(map(int, input().split()))

import math
def comb(M, N):
    if M<0: return 0
    if M<N: return 0
    return (math.factorial(M)//(math.factorial(M-N)*math.factorial(N)))

print(comb(S+2, 2)-3*(comb(S+2-K-1, 2))+3*(comb(S+2-2*(K+1), 2)))
