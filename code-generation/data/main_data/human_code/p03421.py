def main(n,a,b):
    if not a*b>=n>=a+b-1:
        return [-1]
    ans=[]
    flg=False
    # ブロック数
    for x in range(b): 
        # x番目のブロック(0-indexed)
        if not flg:
            for y in range(a):
                # x*a+y+1個目の要素(1-indexed)
                ans.append(b-x+b*y)
                if len(ans)+(b-x)==n:
                    if y!=a-1:
                        ans.append(b-x+b*(a-1))
                    else:
                        ans.append(b-(x+1))
                    flg=True
                    break
        elif flg:
            ans.append(b-x+b*(a-1))
    c=ans.copy()
    c.sort()
    from bisect import bisect_right
    ans=[bisect_right(c,x) for x in ans]
    return ans

n,a,b=map(int,input().split())
ary=main(n,a,b)
print(*ary,sep=' ')
