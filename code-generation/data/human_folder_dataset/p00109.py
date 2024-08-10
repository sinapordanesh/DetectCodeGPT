def digit():
    global S
    global cur
    if S[cur].isdigit():
        n = int(S[cur])
        cur += 1
        return n
def number():
    global S
    L = len(S)
    global cur
    n = digit()
    while (cur < L and S[cur].isdigit()):
        n = n*10 + digit()
    return n
def expression():
    global S
    global cur
    L = len(S)
    a = term()
    while (cur < L and (S[cur] == '+' or S[cur] == '-')):
        op = S[cur]
        cur += 1
        b = term()
        if op == '+':
            a += b
        else:
            a -= b
    return a
import math
def term():
    global S
    global cur
    L = len(S)
    a = factor()
    while (cur < L and (S[cur] == '*' or S[cur] == '/')):
        op = S[cur]
        cur += 1
        b = factor()
        if op == '*':
            a *= b
        else:
            a = math.trunc(a/b)
    return a
def factor():
    global S
    global cur
    if (S[cur] != '('):
        return number()
    else:
        cur += 1
        n = expression()
        if S[cur] == ')':
            cur += 1
            return n

N = int(input().strip())
for _ in range(N):
    S = str(input().strip())
    S = S[:-1]
    cur = 0
    ans = expression()
    print(ans)

