n = int(input())
f = []
p = []
for _ in range(n):
  f.append(list(map(int, input().split())))
for _ in range(n):
  p.append(list(map(int, input().split())))

def solve(out_list):
  ans = 0
  for fi, pi in zip(f, p):
    c = 0
    for o in out_list:
      if fi[o] == 1:
        c += 1
    ans += pi[c]
  return ans

ans = -float("inf")
for i in range(2 ** 10):
  out_list = []
  ## どの桁が1になっているかをチェックするために2進数の各桁をループ
  for j in range(10):
    ## i >> jで確認したい桁を一番右までずらして1と論理積をとって「選択」している要素を確認
    if (i >> j) & 1:
      out_list.append(j)
  if len(out_list) != 0:
    ans = max(ans, solve(out_list))
print(ans)
