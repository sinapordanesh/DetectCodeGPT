def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
s = list(map(int, input().split()))

D = [[]]
for i in range(1, N):
  DD = []
  T = [0]
  for j in range(i, N, i):
    T.append(T[-1] + s[j])
  DD.append(T)
  T = [0]
  start = (N - 1) % i
  if start == 0: start += i
  for j in range(start, N, i):
    T.append(T[-1] + s[j])
  DD.append(T)
  D.append(DD)

ans = s[-1]
cnt = 0
for n in range(2, N - 1):
  end = N - 1 - n
  for m in make_divisors(end):
    if n <= m: break
    if n % m == 0 and end >= n: continue
    k = end // m
    a = D[m][0][k]
    l = len(D[m][1])
    b = D[m][1][-1] - D[m][1][l - k - 2]
    ans = max(ans, a + b)

print(ans)