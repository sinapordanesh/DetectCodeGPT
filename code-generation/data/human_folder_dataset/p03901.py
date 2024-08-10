import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 偶奇をあわせて寄せていくだけ

X,P = map(int,read().split())

def f(x):
    y = x // 2
    return y * 100 / P

if X % 2 == 0:
    answer = f(X)
else:
    answer = 1 + (P * f(X-1) + (100-P) * f(X+1))/100

print(answer)

