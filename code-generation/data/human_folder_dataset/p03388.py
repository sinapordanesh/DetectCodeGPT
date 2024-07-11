Q = int(input())

def derive_k(n):#n/k - n/(k+1) >= 1となる最大のkを求める。ただしn>=2
  if n == 1:
    return 0
  lt = 1
  rt = n
  while rt - lt > 1:
    ct = (lt + rt) // 2
    if n >= ct * (ct+1):
      lt = ct
    else:
      rt = ct
  return lt  
  
for _ in range(Q):
  A, B = map(int,input().split())
  k = derive_k(A*B) #A*B/k - A*B/(k+1) >= 1となる最大のkを求める
  ans = k + (A*B-1)//(k+1) - 1
  #print(A, B, k, (A*B-1)//(k+1))
  if k+1 == A and k*(k+1) < A*B:
    ans += 1
  print(ans)
  
