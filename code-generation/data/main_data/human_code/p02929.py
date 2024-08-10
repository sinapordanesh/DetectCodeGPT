import sys

mod = 10 ** 9 + 7

N = int(input())
S = input()

if S[0] == 'W' or S[-1] == 'W':
    print(0)
    sys.exit()

d = {'L':'R', 'R':'L'}

T = 'L'
for i in range(2 * N-1):
    if S[i] == S[i+1]:
        T += d[T[-1]]
    else:
        T += T[-1]

if T.count('L') != N:
    print(0)
    sys.exit()

ans = 1
cnt = 0

for i in range(2 * N):
    if T[i] == 'L':
        cnt += 1
    else:
        ans *= cnt
        ans %= mod
        cnt -= 1

def factorial(n, mod):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
        fact %= mod
    return fact

ans *= factorial(N, mod)
ans %= mod

print(ans)