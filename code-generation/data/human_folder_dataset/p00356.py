def gcd(p,q):
      if p<q:
            return gcd(q,p)
      if p%q==0:
            return q
      else:
            return gcd(q,p%q)

x,y = map(int,list(input().split(" ")))
print(x+y+1-gcd(x,y))

