def slv(n,ab):
    if [a for a,b in ab]==[b for a,b in ab]:return 0
    c=[]
    W=0
    ret=0
    for i,(a,b) in enumerate(ab):
        # どれだけの要素を0にできるか。
        # 0にできない要素の和を最小化する。
        # a<=bとなっているところは0にできる
        if a-b>0:
            c.append([b,a-b])
        else:
            ret+=b
            W+=b-a
    W-=1
    # ナップザック問題？
    # c=[v,w],W:
    # 価値v重さwの商品配列c、最大容量Wのナップザックに入る最大価値は
    # ナップザックに入るcの要素を0にできる
    # |c|<=10^5 v,w<=10^9 W<=10^14,sum(w)-1==W
    # sum(w)-1==Wより、はいらない商品は1つだけ。vの小さい商品をのこして他は入れればよい
    # dp不要
    c.sort(key=lambda x:x[0])
    ret+=sum([v for v,w in c[1:]])
    return ret



n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
print(slv(n,ab))
