'''
Created on 2020/08/23

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin())
  H=list(map(int,pin().split()))
  H.reverse()
  for i in range(N-1):
    if H[i]>=H[i+1]:
      pass
    elif H[i]==H[i+1]-1:
      H[i+1]-=1
    else:
      print("No")
      break
  else:
    print("Yes")
  return 

main()