A, B = map(int, input().split())
# 消費税8%でA円、10%のときB円の消費税が課される
# 税抜き価格は？
# 小数点以下切り捨て

# 税抜きx円
def tax(x):
  return 8 * x // 100, 10 * x // 100

# A = |.08x|
# B = |.10x|

# x >= A / 1.08
# x >= B / 1.10

x = int(min(A / 0.08, B / 0.1))
Xmax = x * 1.5
while x <= Xmax:
  a, b = tax(x)
#  print(x, a, b)
  if a == A and b == B:
    print(x)
    break
  x += 1
else:
  print(-1)