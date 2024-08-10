# folk from submission 2019-11-19 16:23:40
# 
# no yorimichi if going back to the shop
# only short cut, no go&back drop
# wait at shop during the number of order <= 1

import time
st_time=time.time()

from heapq import heappush, heappop, heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
ts=time.time()
sys.setrecursionlimit(10**6)
#input=sys.stdin.readline

show_flg=False
show_flg=True
drop_probability=1

def dijkstra(edge,st):
    # initialize: def: d=dist(st,i), prev=[previous vertex in minimum path], q[]
    n=len(edge)
    d=[(0 if st==i else inf,i) for i in range(n)]
    prev=[0]*n
    q=[i for i in d]
    heapify(q)
    
    # calc
    while q:
        dist,cur=heappop(q)
        for dst,dist in edge[cur]:
            alt=d[cur][0]+dist
            if alt<d[dst][0]:
                d[dst]=(alt,dst)
                prev[dst]=cur
                heappush(q,(alt,dst))
    dist=[i for i,j in d]
    return dist,prev

V,E=MI()
g=[[] for _ in range(V+1)]
c=[]
neighber=[set() for _ in range(V+1)]
d_map=[{} for _ in range(V+1)]
for i in range(E):
    u,v,d=MI()
    g[u].append((v,d))
    g[v].append((u,d))
    c.append((u,v,d))
    neighber[u].add(v)
    neighber[v].add(u)
    d_map[u][v]=d
    d_map[v][u]=d

mins=[[] for _ in range(V+1)]
prevs=[[] for _ in range(V+1)]
for i in range(1,V+1):
    min_dist,prev=dijkstra(g,i)
    mins[i]=min_dist
    prevs[i]=prev

f=LI()
T=I()
order=[0]*T
accor=[0]*T
order_time=[]

#show('order',order)
order_at_shop=[] # stock (vertex, order_time)
item_at_car=[[] for _ in range(V+1)] # stock order time at each vertex
num_item_at_car=0

def ship():
    global num_item_at_car
    while order_at_shop:
        v,t=order_at_shop.pop()
        item_at_car[v].append(t)
        num_item_at_car+=1
##    show('item_at_car',item_at_car)

def deliver(v,deliver_t):
    global num_item_at_car
    d_p=0
    while item_at_car[v]:
        or_t=item_at_car[v].pop()
        num_item_at_car-=1
        d_p+=T**2-(deliver_t-or_t)**2
##    show("delivered to",v,"deliverPoint",d_p)
    return d_p

def stat_init():
    global order_at_shop
    global item_at_car
    global num_item_at_car
    order_at_shop=[] # stock (vertex, order_time)
    item_at_car=[[] for _ in range(V+1)] # stock order time at each vertex
    num_item_at_car=0

def root_valuator(current,now,root,f_info=True):
    if len(root)==0:
        return 0,0
    global item_at_car
    cur=current
    point=0
    rt=now
    for next_dest,dist in root[::-1]:
        if len(item_at_car[next_dest])>0:
            rt+=dist
            for j in item_at_car[next_dest]:
                point+=T**2-(rt-j)**2
        cur=next_dest
    return point,rt-now
    

def neighber_search(cur,next_dest,effc,best_p,best_d,f_info=True):
    global item_at_car
    drop=[]
    n_item=0
    for nb,dist in g[cur]:
        if nb==next_dest:continue
        if len(item_at_car[nb])>n_item:
            n_item=len(item_at_car[nb])
            drop_effc=(best_p+n_item*(T**2))/(mins[cur][nb]*2+best_d)
            #if random.random()<drop_effc/effc:
            if drop_effc>=effc:
                drop=[(cur,mins[nb][cur]),(nb,mins[cur][nb])]
    return drop

def optimizer_drop(current,now,root,effc,best_p,best_d,f_info=True):
##    show('!Optimizing',root)
    global item_at_car
    opt_root=[]
    cur=current
    org_now=now
    org_effc=effc
    n=len(root)
    
    for i in range(1,n+1):
        next_dest,dist=root[-i]
        drop=[]
        alt=0
        n_item=0
        for nb,d_nb in g[cur]:
            if nb==next_dest:continue
            if len(item_at_car[nb])>n_item:
                #n_item=len(item_at_car[nb])
                rt=now+d_nb
                for j in item_at_car[nb]:
                    alt+=T**2-(rt-j)**2
                if prevs[nb][next_dest]==nb: # nb connected to next_dest ( possible enhancement mins[prevs[nb][next_dest]][next_dest]==mins[nb][next_dest] )
                    drop_time=mins[cur][nb]+mins[nb][next_dest]-dist
                    drop_effc=(best_p+alt)/(drop_time+best_d)
                    if drop_effc>=effc:
                        effc=drop_effc
                        #effc=drop_effc
                        drop.append((nb,mins[cur][nb]))
                        drop.append((next_dest,mins[nb][next_dest]))
                elif 0==1:
                    drop_time=mins[cur][nb]*2
                    drop_effc=(best_p+alt)/(drop_time+best_d)
                    if drop_effc>=effc:
                        effc=drop_effc
                        #effc=drop_effc
                        drop.append((nb,mins[cur][nb]))
                        drop.append((cur,mins[nb][cur]))
                        drop.append((next_dest,mins[cur][next_dest]))
        
        if drop:
            opt_root+=drop
            now+=drop_time
##            show('#yorimichi',drop)
        else:
            opt_root.append((next_dest,dist))
            now+=dist
        cur=next_dest
    
    # opt_root validation
    opt_valid=True
    cur=current
    for next_dest,dist in opt_root:
        if next_dest in neighber[cur]:
            if d_map[cur][next_dest]!=dist:
                opt_valid=False
            else:
                0 # validation ok
        else:
            opt_valid=False
        
        cur=next_dest
    
    if opt_valid:
        p,t=root_valuator(current,org_now,opt_root,f_info=False)
        opt_effc=p/t if t!=0 else 0
        if org_effc<=opt_effc:
            rt=opt_root[::-1]
        else:
            rt=root
    else:
##        show('!!optimization failed')
        rt=root
    
    return rt


def best_deliver(cur,now,f_info=True):
    global order_at_shop
    global item_at_car
    global num_item_at_car
    effc=0
    best_p,best_d=0,inf
    deliver_point=1
    # direct go
    for dest in range(2,V+1):
        if dest==cur:continue
        d=mins[cur][dest]
        rt=now+d
        alt=0
        for j in item_at_car[dest]:
            alt+=T**2-(rt-j)**2
        if alt/d>effc:
            effc,best_p,best_d=alt/d,alt,d
            deliver_point=dest
    # turn to shop and go
    if cur!=1:
        db=mins[cur][1]
        nx_item_at_car=[[] for i in range(1+V)]
        for order_v,t in order_at_shop:
            nx_item_at_car[order_v].append(t)
        for i in range(2,1+V):
            for t in item_at_car[i]:
                nx_item_at_car[i].append(t)
        if f_info:
            for t in range(min(now+1,T-1),min(now+db+1,T)):
                v=order[t]
                if v!=0:
                    nx_item_at_car[v].append(t)
        for dest in range(2,V+1):
            if cur==1:break
            if dest==cur:continue
            dg=mins[1][dest]
            rt=now+db+dg
            d=db+dg
            alt=0
            for j in nx_item_at_car[dest]:
                alt+=T**2-(rt-j)**2
            if alt/d>effc:
                effc,best_p,best_d=alt/d,alt,d
                deliver_point=1
            
    # generate root
    root=[]
    p=deliver_point
    while p!=cur:
        prev_p=prevs[cur][p]
        root.append((p,mins[p][prev_p]))
        p=prev_p
    
    # optimize
    if deliver_point==1:
        0
    else:
        root=optimizer_drop(cur,now,root,effc,best_p,best_d,f_info=False)
    # opt end

    return deliver_point,root,effc

# recieve info
def interactive(wait_num):
    stat_init()
    move=[]
    state=0 # 0 on vertex, 1 on road
    reached=False # True if reached at final destination
    final_dest=1
    dest=1
    cur=1
    point=0
    effc=0
    
    for t in range(T):
        Nnew=I()
        v=0
        for j in range(Nnew):
            new_id,v=MI()
        Nput=I()
        for j in range(Nput):
            put_id=I()

        order[t]=v
        if v!=0:
            order_at_shop.append((v,t))
        if cur==1 and state==0:
            ship()
        if num_item_at_car<=wait_num and cur==1 and state==0:
            print(-1)
            sys.stdout.flush()
            ship()
        else:
            if state==0:
                if dest==1: # 店で荷物を積載
                    ship()
                else: # 配達完了
                    point+=deliver(dest,t)

                if cur==final_dest:
                    # set final destination
                    final_dest,root,effc=best_deliver(cur,t)
##                    show('root setting',root)
                else:
                    0
                dest,dist=root.pop()
                state=1
            else: # on road at teh begining
                0
            print(dest)
            sys.stdout.flush()
            dist-=1
##            show('moving to',dest,'root',root)
            if dist==0:
                state=0
                cur=dest

        vardict = input()
        if vardict == 'NG':
            for i in range(10**13):
                aa=[1,2]
                bb=aa.pop()+1
            sys.exit()

        Nachive = int(input())
        for j in range(Nachive):
            achive_id=I()

    return point


mode='rand'
mode='greed'
if mode=='rand':
    time_limit=29.5 # 1 = 1 sec
    time_limit=0.07
    now=time.time()
    p=-1
    s=T//2
    c=1
    while True:
        c+=1
        now=time.time()
        if now - st_time > time_limit:
            break
        cur_p,cur_st,cur_move=rand_move(s,c)
        if cur_p>p or p==-1:
            p=cur_p
            s=cur_st
            move=cur_move
elif mode=='greed':
    point=interactive(wait_num=1)
