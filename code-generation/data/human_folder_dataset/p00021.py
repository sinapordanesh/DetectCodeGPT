E = 10 ** -10
def check(lst):
  x1, y1, x2, y2, x3, y3, x4, y4 = lst
  vabx, vaby = x2 - x1, y2 - y1
  vcdx, vcdy = x4 - x3, y4 - y3
  if abs(vabx * vcdy - vcdx * vaby) < E:
    return True
  else:
    return False

n = int(input())
for _ in range(n):
  plst = list(map(float, input().split()))
  print("YES" if check(plst) else "NO")
