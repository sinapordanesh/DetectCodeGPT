def main(n,k,ab):
  ks=[k]
  m=len(bin(k))-2
  # kはm桁
  kbin=bin(k)[2:]
  now=0
  for i in range(m):
    if kbin[i]=='1' and i<m-1:
      ks.append(now+pow(2,m-i-1)-1)
    now+=int(kbin[i])*pow(2,m-i-1)
  ans=0
  for x in ks:
    tmp=0
    for a,b in ab:
      if a|x==x:tmp+=b
    ans=max(ans,tmp)
  print(ans)

n,k=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
main(n,k,ab)