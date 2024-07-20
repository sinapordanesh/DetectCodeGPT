class BellmanFord:
    INF = int(1e18)
    N = -1
    edge = []
    
    def __init__(self, N):
        self.N = N
        
    def add_edge(self, frm, to, cost):
        self.edge.append((frm, to, cost));
        
    def add_bi_edge(self, a, b, cost):
        self.add_edge(a, b, cost)
        self.add_edge(b, a, cost)
    
    def calcD(self, start):
        D = [self.INF] * self.N
        D[start] = 0
        update, cnt = True, 0
        while update:
            update = False
            cnt = cnt + 1
            if cnt > self.N:
                return 'NegativeCycle'
            
            for frm, to, cost in self.edge:
                ncost = D[frm] + cost
                if D[frm] == self.INF or ncost >= D[to]:
                    continue
                D[to] = ncost
                update = True
                
        return D

    
V, E, S = list(map(int, input().split()))
bf = BellmanFord(V)
for i in range(E):
    frm, to, cost = list(map(int, input().split()))
    bf.add_edge(frm, to, cost)
    

ans = bf.calcD(S)
if ans == 'NegativeCycle':
    print("NEGATIVE CYCLE")
else:
    for i in range(V):
        print ('INF' if ans[i] == bf.INF else ans[i])

