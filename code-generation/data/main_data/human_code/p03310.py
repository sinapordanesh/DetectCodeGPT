import sys
readline = sys.stdin.readline

# 累積和によって、各区間の和をO(1)で求められるようにしておく
# B,C,D,Eに分けたときに、CとDの切れ目を固定する
# Cの終わりが決まったとき、Bを先頭から探索していくとB,Cを切るベストな点が分かる
# （BとCの絶対値の差が最小になる点）
# 同様に、CとDを切るベストな点が分かる
# これらのindexを覚えておくと、CとDの切れ目を移動したときにこの点から開始することが出来て
# O(N)の定数倍で解くことが出来る

N = int(readline())
A = [0] + list(map(int,readline().split()))
for i in range(1, len(A)):
  A[i] += A[i - 1]

#print(A)

b_end = 1
c_end = 2
d_end = 3
e_end = len(A) - 1
bc_best = 10 ** 10
de_best = 10 ** 10
ans = 10 ** 10
def get_ans(b_end,c_end,d_end):
  B = A[b_end]
  C = A[c_end] - A[b_end]
  D = A[d_end] - A[c_end]
  E = A[-1] - A[d_end]
#  print("get_ans b_end",b_end,"c_end",c_end,"d_end",d_end)
#  print("get_ans B",B,"C",C,"D",D,"E",E)
  return max(B,C,D,E) - min(B,C,D,E)

for c_end in range(2, N - 1):
  # b_endを右に進める条件は、今BよりCのほうが大きいこと 且つ c_endに追いつかないこと
  # Bのほうが大きくなったら、その直前と比べてどっちのほうが絶対値が小さいかを確認する
  B = A[b_end]
  C = A[c_end] - A[b_end]
  best_b_end = b_end
  if B != C:
    while b_end + 1 < c_end and B < C:
      b_end += 1
      tempB = B
      tempC = C
      B = A[b_end]
      C = A[c_end] - A[b_end]
      if B == C:
        best_b_end = b_end
        break
      if B > C:
        # ここでBのほうが大きくなったら有利なほうを採用する
        if abs(tempB - tempC) > abs(B - C):
          best_b_end = b_end
        break
      else:
        best_b_end = b_end
  b_end = best_b_end
  
  D = A[d_end] - A[c_end]
  E = A[e_end] - A[d_end]
  best_d_end = d_end
  if D != E:
    while d_end + 1 < e_end and D < E:
      d_end += 1
      tempD = D
      tempE = E
      D = A[d_end] - A[c_end]
      E = A[e_end] - A[d_end]
      if D == E:
        best_d_end = d_end
        break
      if D > E:
        if abs(tempD - tempE) > abs(D - E):
          best_d_end = d_end
        break
      else:
        best_d_end = d_end
  d_end = best_d_end
    
  val = get_ans(b_end,c_end,d_end)
  if val < ans:
    ans = val
    
print(ans)