def main():
  n = int(input())
  ans = 0
  for k in divisors(n):
    if k == 1:
      continue
    if check(n, k):
      ans += 1
  ans += len([None for k in divisors(n-1) if k != 1])
  print(ans)

def check(original_n, k):
  n = original_n
  while n % k == 0:
    n = n // k
  n = n % k
  return n == 1

def divisors(n):
  result = []
  for i in range(1, n+1):
    if i*i > n:
      break
    if n%i == 0:
      result.append(i)
      d = n // i
      if d != i:
        result.append(d)
  return result


main()