n=int(input())
a=[int(input()) for _ in range(n)]
def main(n,a):
  pre=0
  ans=0
  for x in a:
    if pre+2<=x:
      # pre+1以上の数値を何回か引き算してxを1以上pre以下にする
      # 引き算の回数はなるべく多く
      if x%(pre+1)==0:
        tmp=x//(pre+1)
        ans+=tmp-1
        pre=max(pre,1)
      else:
        tmp=x//(pre+1)
        ans+=tmp
        pre=max(pre,x%(pre+1))
    else:
      pre=max(pre,x)
  print(ans)
main(n,a)
