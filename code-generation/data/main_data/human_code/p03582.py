def work(a,b,c,A,B,C):
 if A==0:
  return work(b,c,'',B,C,0)
 if B==0:
  if C==0:
   return a*A
  else:
   return work(a,c,'',A,C,0)
 if C==0:
  return work(a+b*(B/A),a+b*(B/A+1),'',A-B%A,B%A,0)
 cmod = C%A
 if B <= A-cmod:
  return work(a+c*(C/A),a+c*(C/A)+b,a+c*(C/A+1),A-cmod-B,B,cmod)
 else:
  bmod = B%(A-cmod)
  return work(a+c*(C/A)+b*(B/(A-cmod)),a+c*(C/A)+b*(B/(A-cmod)+1),a+c*(C/A+1),A-bmod-cmod,bmod,cmod)

if __name__ == '__main__':
 s = raw_input()
 a,b,c = [int(i) for i in s.split()]
 print(work('a','b','c',a,b,c))
