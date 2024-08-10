def main(n,q,a,x):
  a.reverse()
  keys=[]
  sums1=[0]
  sums2=[0]
  tmp1=0
  tmp2=0
  for i in range(n):
    if i%2==0:tmp1+=a[i]
    tmp2+=a[i]
    sums1.append(tmp1)
    sums2.append(tmp2)
  sums=[]
  for i in range((n-1)//2):
    k=a[i+1]+a[i+1+(i+1)]
    keys.append(k//2+1)
    # 
    s=sums2[i+1]+sums1[-1]-sums1[i+1+(i+1)]
    sums.append(s)
  sums.append(sums2[(n+2-1)//2])
  keys.append(0)
  sums.reverse()
  keys.reverse()
  from bisect import bisect_right
  #print(sums)
  #print(keys)
  for xx in x:
    idx=bisect_right(keys,xx)-1
    print(sums[idx])



n,q=map(int,input().split())
a=list(map(int,input().split()))
x=[int(input()) for _ in range(q)]
main(n,q,a,x)
