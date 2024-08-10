def min_diam(A,B,C): # returns a "diameter"
  segments=[A,B,C]
  segments.sort()
  return (segments[0]**2+segments[1]**2)**(1/2)

while True:
  # input one dataset
  A,B,C = tuple(map(float,input().split()))
  if (A,B,C) == (0,0,0):
    break
  n = int(input())
  R = [None]*n
  for i in range(n):
    R[i] = float(input())
  # process
  diam = min_diam(A,B,C)
  # judge & output
  for r in R:
    if diam < 2*r:
      print("OK")
    else:
      print("NA")