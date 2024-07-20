#####segfunc#####
def segfunc(x, y):
    return min(x,y)
#################

#####ide_ele#####
ide_ele = float("inf")
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def main():
    import sys,random

    input=sys.stdin.readline

    N=int(input())
    q=[]
    r=[]
    b=[]
    X=0
    q_append=q.append
    for i in range(N):
        x,y=map(int,input().split())
        r.append(max(x,y))
        b.append(min(x,y))


    X=max(b)
    init_val=[b[i] for i in range(N)]
    for i in range(N):
        x,y=r[i],b[i]
        if X>r[i]:
            init_val[i]=r[i]
        elif X>b[i]:
            q_append((r[i],i,-1))
            init_val[i]=b[i]
        else:
            q_append((b[i],i,1))
            q_append((r[i],i,-1))
            init_val[i]=b[i]

    q.sort()
    test1=float("inf")
    rmq=SegTree(init_val,segfunc,ide_ele)
    

    for i in range(0,len(q)):
        val,index,k=q[i]
        if k==-1:
            rmq.update(index,val)
        res=rmq.query(0,N)
        test1=min(val-res,test1)


    test2=(max(r)-min(r))*(max(b)-min(b))
    test1*=(max(max(b),max(r))-min(min(b),min(r)))
    print(min(test1,test2))

if __name__=="__main__":
    main()
