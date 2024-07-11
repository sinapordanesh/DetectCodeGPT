import sys
def S(): return sys.stdin.readline().rstrip()


S,T = S(),S()
print(sum(S[i] == T[i] for i in range(3)))
