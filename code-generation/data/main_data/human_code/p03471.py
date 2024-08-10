def main():
  n, y = map(int, input().split())
  y //= 1000
  for i in range(n + 1):
    if i * 10 > y:
      break
    for j in range(n + 1):
      if i * 10 + j * 5 > y:
        break
      k = n - i - j
      if i * 10 + j * 5 + k == y:
        print(i, j, k)
        return
  print(-1, -1, -1)

main()