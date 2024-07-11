from collections import defaultdict
def main():
  N, K = map(int,input().split())
  D = defaultdict(int)
  for _ in range(N):
    a, b = map(int,input().split())
    D[a]+=b
  D = sorted(D.items())
  ans, total = D[0]
  for i in range(1,len(D)):
    if K <= total:
      print(ans)
      return
    else:
      c, d = D[i]
      ans = c
      total+=d
  print(ans)
  return

main()