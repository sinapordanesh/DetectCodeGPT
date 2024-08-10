def solve():
    from itertools import product
    from sys import stdin
    f_i = stdin
    
    while True:
        P, M = map(int, f_i.readline().split())
        if P == 0:
            break
        
        bingo = []
        for i in range(P):
            b = []
            card = list(map(int, f_i.readline().split()))
            d1 = [] # diagonally
            d2 = [] # diagonally
            for i in range(M):
                b.append(card[i::M]) # vertically
                b.append(card[i*M:i*M+M]) # horizontally
                d1.append(card[i*M+i])
                d2.append(card[(M-1)*(i+1)])
            
            b += [d1, d2]
            bingo.append(set(frozenset(b_i) for b_i in b))
        if P == 2:
            ans = min(len(t1 | t2) for t1, t2 in product(*bingo))
        elif P == 3:
            ans = P * M + 1
            c0, c1, c2 = bingo
            for b0 in c0:
                if b0 in c2:
                    for b1 in c1:
                        if b1.intersection(b0):
                            break
                    else:
                        continue
                
                for b1 in c1:
                    b01 = b0.union(b1)
                    last = set(b for b in c2 if b.issubset(b01))
                    if last:
                        if not b1.intersection(*last):
                            continue
                    for b2 in c2:
                        tmp = len(b2.union(b01))
                        if tmp < ans:
                            ans = tmp
            if ans == P * M + 1:
                ans = 0
        else:
            ans = P * M + 1
            c0, c1, c2, c3 = bingo
            for b0 in c0:
                if b0 in c2:
                    for b1 in c1:
                        if b1.intersection(b0):
                            break
                    else:
                        continue
                
                if b0 in c3:
                    for b1, b2 in product(c1, c2):
                        if b0.intersection(b1, b2):
                            break
                    else:
                        continue
                for b1 in c1:
                    b01 = b0.union(b1)
                    third = set(b2 for b2 in c2 if b2.issubset(b01))
                    if third:
                        if not b1.intersection(*third):
                            continue
                    
                    last = set(b3 for b3 in c3 if b3.issubset(b01))
                    if last:
                        if not b1.intersection(*last):
                            continue
                    
                    if third and last:
                        if not b1.intersection(*third, *last):
                            continue
                    
                    if not third and last:
                        for b2, b3 in product(c2, last):
                            if b1.intersection(b2, b3):
                                break
                        else:
                            continue
                    for b2 in c2:
                        b012 = b0.union(b1, b2)
                        last = set(b for b in c3 if b.issubset(b012))
                        if last:
                            last_num = b2.intersection(*last)
                            if not last_num:
                                continue
                            
                            first = set(b for b in c0 if b.issubset(b012))
                            if first.issubset(last):
                                sec = set(b for b in c1 if b.issubset(b012))
                                if not last_num.intersection(*sec):
                                    continue
                        for b3 in c3:
                            tmp = len(b012.union(b3))
                            if tmp < ans:
                                ans = tmp
            if ans == P * M + 1:
                ans = 0
        
        print(ans)

solve()
