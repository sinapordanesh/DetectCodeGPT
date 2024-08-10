def get_cycle(pre, nxt, root):
    cycles, checked = [], set()

    # root?????£????????????????????????????????§?????????????????????
    checked |= {root}
    que = nxt[root][:]
    while que:
        root_linked = que.pop()
        checked |= {root_linked}
        if nxt[root_linked]:
            que.extend(nxt[root_linked])

    for i in range(len(pre)):
        if i in checked:
            continue

        # ?????°????????§???????????????????????????
        checking = set()
        while i not in checked:
            checked |= {i}
            checking |= {i}
            i = pre[i]
        if i not in checking: # ?????°????????????
            continue

        # ??????????????´???????????????????????°??¨????????¢???   
        checking.clear()
        while i not in checking:
            checking |= {i}
            i = pre[i]            
            
        cycles.append(checking)
    return cycles

def cycle_cost(cycles, m):
    return sum(m[ci] for cycle in cycles for ci in cycle)

from collections import defaultdict
from itertools import product
def chi_liu_edmonds(g, v, r):
    # ?°??????????????????????????±??????????
    m = [float('inf')] * v
    pre = [None] * v
    for s, t in product(range(v), repeat=2):
        if g[s][t] < m[t]:
            m[t] = g[s][t]
            pre[t] = s
    nxt = defaultdict(list)
    for t, s in enumerate(pre):
        if s is not None:
            nxt[s].append(t)

    cycles = get_cycle(pre, nxt, r)

    # ??¨??¨??£?????????????????´???
    if len(cycles) == 0:
        m[r] = 0
        return sum(m)
    
    not_cycle = set(range(v)).difference(*cycles)
    #????´????????????????
    abridger  = {ni:i for i, ni in enumerate(not_cycle)}
    abridger.update({ci:i + len(not_cycle) for i, cycle in enumerate(cycles) for ci in cycle})
    v_dash = len(not_cycle) + len(cycles)
    g_dash = [[float('inf')] * v_dash for _ in range(v_dash)]
    for s, t in product(range(v), repeat=2):
        s_dash, t_dash = abridger[s], abridger[t]
        if s_dash != t_dash:
            d = g[s][t] if t in not_cycle else g[s][t] - g[pre[t]][t]
            if g_dash[s_dash][t_dash] > d:
                g_dash[s_dash][t_dash] = d
    return chi_liu_edmonds(g_dash, v_dash, abridger[r]) + cycle_cost(cycles, m)

from sys import stdin
readline = stdin.readline

v, e, r = map(int, readline().split())
g = [[float('inf')] * v for _ in range(v)]

for _ in range(e):
    s, t, d = map(int, readline().split())
    if t == r:
        continue
    g[s][t] = d
print(chi_liu_edmonds(g, v, r))