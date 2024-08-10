import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
奇閉路がないので二部グラフ
まずは最大の二部グラフを作る．
左右それぞれのグループ内の頂点同士を結ぶ辺がない．
この時点でスケールの小さい同問題に帰着，グループ内で二部グラフを作れば良い．
ただ，これを素直にやると構築が面倒そう．

レベルの最大値の最小値はN<=2^mなる最小のm
つまりNの二進数表記での桁数

レベル1 : 000..111...
レベル2 : 00..11..00..11..
みたいに分けるか．
これ，二進数で各bitが異なる頂点とつなげば良い．すでにあるならば無視
"""
def main():
    mod=10**9+7
    N=I()
    M=2**(N-1).bit_length()
    
    ans=[[-1]*N for _ in range(N)]
    
    for k in range(M):#二進数の桁数
        for i in range(N):
            for j in range(i+1,N):
                if (i>>k &1)^(j>>k &1):#iとjのkbit目が違うならば
                    if ans[i][j]==-1:
                        ans[i][j]=k+1
                        
    for i in range(N):
        print(' '.join(map(str, ans[i][i+1:])))
    
    

main()
