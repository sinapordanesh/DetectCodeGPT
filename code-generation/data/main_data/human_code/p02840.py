import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
Sの通り数で良い

X+D ~ X+(N-1)*D まで
a個とったとして，aX + bDの形になる.add()
Dの個数bについて，minとmaxを考えれば，その間は全部作れるはず

N,X,D=5,4,2
[4,6,8,10,12]からa=3個選ぶ場合
3X+3D ~ 3X+9Dまでの7通り作れる，

a個選ぶ場合，Dの係数は
min b : (a-1)*a // 2            ... 0~(a-1)までの和
max b  : a*(N-1) - (a-1)*a // 2      ... (N-a)~(N-1)までの和

通り数： a*(N-1) - 2*((a-1)*a // 2) + 1

ここからXとDが変動した時のかぶりをどうするか

aを決め打つと，表せる範囲は等差数列になる（等差D）
結局，いろんな等差数列が出てくるのでそれらで表せるものを探す．

min b = L
max b = Rとする
RーL = R'とする
初項Ca = a*X + D*Lとする

この数列はCa ~ Ca + D*R'

(a*X)mod D の値が異なれば絶対に同じ値にはならない
mod Dごとにグループを分けて考える，
各グループでCa/D =Ca'として
Ca' ~ Ca'+R'　の区間を考える．どこかの区間に入っていればOK
=>イベントソート，+1と−１

"""
def main():
    N,X,D=MI()
    if D==0:
        if X==0:
            print(1)
            exit()
        else:
            print(N+1)
            exit()
            
    #グルーピング
    from collections import defaultdict
    dd = defaultdict(list)
    for a in range(N+1):
        L = ((a-1)*a)//2
        R = a*(N-1) - ((a-1)*a)//2
        R2 = R-L
        Ca = a*X + D*L
        key=(a*X)%D
        dd[key].append([Ca//D , Ca//D + R2])
        
    #イベントそーと
    ans=0
    for k,vs in dd.items():
        E=[]
        for v in vs:
            E.append([v[0],1])
            E.append([v[1]+1,-1])
        E.sort()
        
        # print(k,vs)
        # print(E)
        
        now=-10**10
        score=0
        for e in E:
            nxt=e[0]
            diff=nxt-now
            if score>=1:
                ans+=diff
            score+=e[1]
            now=nxt
            
    print(ans)
            
            
        
    


    

main()
