def solve():
  w, h = map(int, input().split())
  base = list(map(int, input().split()))
  if abs(2 * base.count(0) - w) >= 2:
    return False
  
  same = 1
  for _ in range(h - 1):
    line = list(map(int, input().split()))
    flag = (base[0] == line[0])
    same += flag
    if flag and line != base:
      return False
    if not flag and any([i == j for i, j in zip(line, base)]):
      return False
  
  return abs(2 * same - h) <= 1

print("yes" if solve() else "no")
