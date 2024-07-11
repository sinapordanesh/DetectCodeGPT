N = int(input())
L = list(map(int, input().split()))
L.sort(reverse = True)

def binary(mini,maxi,a,b): #a>b
  if maxi == mini + 1:
    if L[maxi] > a - b:
      return maxi
    elif L[mini] > a - b:
      return mini
    else:
      return False
  elif maxi == mini:
    if L[maxi] > a - b:
      return maxi
    else:
      return False
  else:
    mid = (mini+maxi)//2
    if L[mid] > a - b:
      return binary(mid,maxi,a,b)
    else:
      return binary(mini,mid,a,b)
ans = 0
for a in range(0, N-2):
  for b in range(a+1, N-1):
    tmp = binary(b+1, N-1, L[a], L[b])
    if tmp:
      ans += tmp - b
print(ans)

