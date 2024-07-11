N = int(input())
S = input()
S1 = S[:N]
S2 = S[N:][::-1]
from itertools import groupby, accumulate, product, permutations, combinations
from collections import defaultdict
def half(S):
  dic = defaultdict(lambda: 0)
  for pro in product([0,1],repeat=N):
    s1 = s2 = ''
    for i,p in enumerate(pro):
      s1 += S[i]*p
      s2 += S[i]*(1-p)
    dic[(s1,s2)] += 1
  return dic
dic1 = half(S1)
dic2 = half(S2)
ans = 0
for k,v in dic1.items():
  ans += v*dic2[k]
print(ans)