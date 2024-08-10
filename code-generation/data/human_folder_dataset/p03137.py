import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,M = MI()
X = LI()

if N >= M:
    print(0)
    exit()

X.sort()
Y = [X[i+1]-X[i] for i in range(M-1)]
Y.sort()
print(sum(Y[:M-N]))
