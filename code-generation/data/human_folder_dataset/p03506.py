N,Q=map(int,input().split())
if N>1:
    def find_par(x):
        u=x%N-1
        if u<=0:
            u+=N
        return (x-u-1)//N+1
    def path(x):
        s_node=x
        d=[s_node]
        while s_node!=1:
            s_node=find_par(s_node)
            d.append(s_node)
        return d
    for _ in range(Q):
        v,w=map(int,input().split())
        data1=set(path(v))
        data2=set(path(w))
        print(max(data1 & data2))
else:
    for _ in range(Q):
        v,w=map(int,input().split())
        print(min(v,w))