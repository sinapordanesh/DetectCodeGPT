import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


q = int(input())
def _sub(a):
    v = []
    for i in range(35):
        a,val = divmod(a,3)
        v.append(val)
    return v
def sub(a,b,c,d):
    va,vb,vc,vd = _sub(a), _sub(b), _sub(c), _sub(d)
    ans = 0
    m1 = True
    m2 = True
    for i in reversed(range(35)):
        aa,bb,cc,dd = va[i],vb[i],vc[i],vd[i]
        if aa==cc==1 and m1 and ((m2 and bb!=dd) or (not m2 and abs(b-d)>2*pow(3,i))):
#             print(aa,bb,cc,dd,m1,m2,i)
            ta = a % pow(3,i)
            tc = c % pow(3,i)
            ans = abs(b-d) + min(ta+tc+2, 2*pow(3,i)-(ta+tc))
            break
        elif bb==dd==1 and m2 and ((m1 and aa!=cc) or (not m1 and abs(a-c)>2*pow(3,i))):
#             print(aa,bb,cc,dd,m1,m2,i)
            tb = b % pow(3,i)
            td = d % pow(3,i)
            ans = abs(a-c) + min(tb+td+2, 2*pow(3,i)-(tb+td))
            break
        else:
            if aa!=cc:
                m1 = False
            if bb!=dd:
                m2 = False
    else:
        ans = abs(a-c) + abs(b-d)
    return ans
ans = [None]*q
for i in range(q):
    a,b,c,d = list(map(lambda x: int(x)-1, input().split()))
    ans[i] = sub(a,b,c,d)
write("\n".join(map(str, ans)))