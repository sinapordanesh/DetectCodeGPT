n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
a_start = [x[0] * 60 + x[1] for x in lst]
a_end = [x[2] * 60 + x[3] for x in lst]
h_start = [x[4] * 60 + x[5] for x in lst]
h_end = [x[6] * 60 + x[7] for x in lst]
b_start = [x[8] * 60 + x[9] for x in lst]
b_end = [x[10] * 60 + x[11] for x in lst]

def make_sets(start, end):
  sets = []
  member = []
  for i in range(1440):
    upd = False
    for j in range(n):
      if start[j] == i:
        member.append(j)
        upd = True
      if end[j] == i - 1:
        member.remove(j)
        upd = True
    if upd:
      sets.append(set(member))
  return sets

a_sets = make_sets(a_start, a_end)
h_sets = make_sets(h_start, h_end)
b_sets = make_sets(b_start, b_end)

ans = 0
for s1 in a_sets:
  for s2 in h_sets:
    for s3 in b_sets:
      ans = max(ans, len(s1 & s2 & s3))

print(ans) 
