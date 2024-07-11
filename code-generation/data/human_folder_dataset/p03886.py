import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import itertools
from heapq import heappop, heapify

N,*A = map(int,read().split())

n90 = sum(x == 90 for x in A)
if n90 - (N-n90) != 4:
    print(-1)
    exit()

x = 0
temp = list(itertools.accumulate(1 if x == 90 else -1 for x in A))
slide = temp.index(min(temp)) + 1
A = A[slide:] + A[:slide]

def F(left_node, right_node, R, depth):
    step = 1<<depth
    # L：左に曲がるインデックス集合
    # R：右に曲がるインデックスのヒープ
    if not R:
        n1,n2,n3,n4 = [i for i,x in enumerate(left_node) if x is not None]
        X = [None] * N
        Y = [None] * N
        X[n1] = step; Y[n1] = 0
        X[n2] = step; Y[n2] = step
        X[n3] = 0; Y[n3] = step
        X[n4] = 0; Y[n4] = 0
        return X,Y
    r = heappop(R); l = left_node[r]
    # l番：90度、r番：270度 を消し飛ばす
    ll = left_node[l]; rr = right_node[r]
    left_node[rr] = ll; right_node[ll] = rr
    left_node[l] = None; left_node[r] = None
    right_node[l] = None; right_node[r] = None
    X,Y = F(left_node,right_node,R,depth+1)
    # 90,270を追加する
    
    dx = X[rr] - X[ll]; dy = Y[rr] - Y[ll]
    if dx > 0:
        Y[rr] += step
        X[l] = X[rr] - step; Y[l] = Y[ll]
        X[r] = X[l]; Y[r] = Y[rr]
    elif dx < 0:
        Y[rr] -= step
        X[l] = X[rr] + step; Y[l] = Y[ll]
        X[r] = X[l]; Y[r] = Y[rr]
    elif dy > 0:
        X[rr] -= step
        X[l] = X[ll]; Y[l] = Y[rr] - step
        X[r] = X[rr]; Y[r] = Y[l]
    elif dy < 0:
        X[rr] += step
        X[l] = X[ll]; Y[l] = Y[rr] + step
        X[r] = X[rr]; Y[r] = Y[l]
    return X,Y

R = [i for i,x in enumerate(A) if x == 270]
heapify(R)

X,Y = F(list(range(-1,N-1)),list(range(1,N))+[0],R,0)

# 最初にずらしていた分
X = X[N-slide:] + X[:N-slide] 
Y = Y[N-slide:] + Y[:N-slide] 

# 最後に座圧して完成
x_to_i = {x:i for i,x in enumerate(sorted(set(X)))}
y_to_i = {y:i for i,y in enumerate(sorted(set(Y)))}
X = [x_to_i[x] for x in X]
Y = [y_to_i[y] for y in Y]

print('\n'.join('{} {}'.format(x,y) for x,y in zip(X,Y)))