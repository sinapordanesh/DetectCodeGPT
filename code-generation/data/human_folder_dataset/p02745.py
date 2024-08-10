def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
aを固定して，b，cの位置を全探索
"""
def main():
    mod=10**9+7
    a=input()
    b=input()
    c=input()
    M=2100

    
    def ch(c1,c2):
        return c1==c2 or c1=="?" or c2=="?"
    
    # aを左端に固定，bがbi文字目から,cが(bからみて)ci文字目から始まるとして，どうなるか
    # 実際にはabcの並びが6通り
    def calc(s1,s2,s3):
        
        # 遠く離れている場合などもokなので，初期値は1，ダメなら0に
        ab=[1]*(2*M)
        ac=[1]*(2*M)
        bc=[1]*(2*M)
        
        Na=len(s1)
        Nb=len(s2)
        Nc=len(s3)
        
        
        for bi in range(Na+5):#aの何文字目から?
            for j in range(Nb):#bの何文字目？
                if bi+j>=Na:
                    break
                if not ch(s1[bi+j], s2[j]):
                    ab[bi]=0
                    break
                
        for ci in range(Na+5):#aの何文字目から?
            for j in range(Nc):#cの何文字目？
                if ci+j>=Na:
                    break
                if not ch(s1[ci+j], s3[j]):
                    ac[ci]=0
                    break
                
        for ci in range(Nb+5):#bの何文字目から?
            for j in range(Nc):#cの何文字目？
                if ci+j>=Nb:
                    break
                if not ch(s2[ci+j], s3[j]):
                    bc[ci]=0
                    break
                
        ans=10**5
        for i in range(Na+5):#bの開始位置
            for j in range(i,Na+Nb+5):#cの開始位置
                if ab[i] and ac[j] and bc[j-i]:
                    temp=max(Na,i+Nb,j+Nc)
                    ans=min(ans,temp)
                    
        # print(ab)
        # print(ac)
        # print(bc)
                    
        return ans
    
    ans=len(a)+len(b)+len(c)
    
    ans=min(ans,calc(a,b,c))
    ans=min(ans,calc(a,c,b))
    ans=min(ans,calc(b,a,c))
    ans=min(ans,calc(b,c,a))
    ans=min(ans,calc(c,a,b))
    ans=min(ans,calc(c,b,a))
    
    print(ans)
                
            

main()
