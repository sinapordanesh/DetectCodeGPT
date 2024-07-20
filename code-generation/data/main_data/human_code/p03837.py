def dijkstra(s):
    import  heapq
    dist=[inf for i in range(n)] #sからの距離のリスト
    dist[s]=0
    mirai=[True for i in range(n)] #Trueなら未確定
    mirai[s]=False

    queue=[] #こいつがheapqになる
    for kyori,to in G[s]:
        heapq.heappush(queue , kyori*10**6+to)  #重みと行先を1つの変数で表してる！
    while queue:
        minedge= heapq.heappop(queue)
        #miraiがTrueのやつ(未確定なやつ)から最小距離のものをさがす
        if not mirai[minedge%(10**6)]: continue
        #距離が小さいものから"確定"していく
        v=minedge%(10**6) #最小距離の頂点
        dist[v] = minedge//(10**6) #その距離
        mirai[v]=False
        for kyori,to in G[v]:
            if mirai[to]:
                heapq.heappush(queue, (kyori+dist[v])*(10**6)+to)
                #queueに入る数は、必ず「sからの」距離と行先を持っている
    return dist
n,m=map(int,input().split())
inf=10**10
G=[[] for i in range(n)]
HEN=[]
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    G[a].append((c,b))
    G[b].append((c,a))
    HEN.append((a,b,c))

MIN=[[10**10]*n for i in range(n)]
for i in range(n):
    MIN[i]=dijkstra(i)
ans=0
for a,b,c in HEN:
    for s in range(n):
        if MIN[s][a]+c == MIN[s][b]:
            break
        if MIN[s][b]+c == MIN[s][a]:
            break
    else:
        ans+=1
print(ans)
