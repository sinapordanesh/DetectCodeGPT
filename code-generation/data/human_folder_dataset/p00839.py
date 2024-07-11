def solve(file_input, x, y):
    exch1 = [] # forward - forward
    exch2 = [] # forward - reverse
    exch3 = [] # reverse - forward
    for i in range(y):
        p, P, space, q, Q = file_input.readline().rstrip()
        p = int(p)
        q = int(q)
        
        if P == 'E':
            if Q == 'W':
                exch1.append((p, q))
            else:
                exch2.append((p, q))
        else:
            if Q == 'E':
                exch1.append((q, p))
            else:
                exch3.append((q, p))
    
    fwd_init = []
    for i in range(x):
        s = file_input.readline().rstrip()
        if s == '-':
            fwd_init.append('')
        else:
            fwd_init.append(s)
    fwd_rec = {'|'.join(fwd_init): 0}
    forwrad = [fwd_init]
    
    bk_init = []
    for i in range(x):
        t = file_input.readline().rstrip()
        if t == '-':
            bk_init.append('')
        else:
            bk_init.append(t)
    bk_rec = {'|'.join(bk_init): 0}
    backward = [bk_init]
    
    for step in range(1, 4):
        tmp_forward = []
        for trains in forwrad:
            for l1, l2 in exch1:
                tmp_trains = trains[:]
                coupled = trains[l1] + trains[l2]
                for i in range(len(coupled) + 1):
                    tmp_trains[l1] = coupled[:i]
                    tmp_trains[l2] = coupled[i:]
                    tmp_state = '|'.join(tmp_trains)
                    if tmp_state not in fwd_rec:
                        if tmp_state in bk_rec:
                            return bk_rec[tmp_state] + step
                        fwd_rec[tmp_state] = step
                        tmp_forward.append(tmp_trains[:])
            for l1, l2 in exch2:
                tmp_trains = trains[:]
                coupled = trains[l1] + trains[l2][::-1]
                for i in range(len(coupled) + 1):
                    tmp_trains[l1] = coupled[:i]
                    tmp_trains[l2] = coupled[i:][::-1]
                    tmp_state = '|'.join(tmp_trains)
                    if tmp_state not in fwd_rec:
                        if tmp_state in bk_rec:
                            return bk_rec[tmp_state] + step
                        fwd_rec[tmp_state] = step
                        tmp_forward.append(tmp_trains[:])
            for l1, l2 in exch3:
                tmp_trains = trains[:]
                coupled = trains[l1][::-1] + trains[l2]
                for i in range(len(coupled) + 1):
                    tmp_trains[l1] = coupled[:i][::-1]
                    tmp_trains[l2] = coupled[i:]
                    tmp_state = '|'.join(tmp_trains)
                    if tmp_state not in fwd_rec:
                        if tmp_state in bk_rec:
                            return bk_rec[tmp_state] + step
                        fwd_rec[tmp_state] = step
                        tmp_forward.append(tmp_trains[:])
        forwrad = tmp_forward
        
        if step == 3:
            return 6
        
        tmp_backward = []
        for trains in backward:
            for l1, l2 in exch1:
                tmp_trains = trains[:]
                coupled = trains[l1] + trains[l2]
                for i in range(len(coupled) + 1):
                    tmp_trains[l1] = coupled[:i]
                    tmp_trains[l2] = coupled[i:]
                    tmp_state = '|'.join(tmp_trains)
                    if tmp_state not in bk_rec:
                        if tmp_state in fwd_rec:
                            return fwd_rec[tmp_state] + step
                        bk_rec[tmp_state] = step
                        tmp_backward.append(tmp_trains[:])
            for l1, l2 in exch2:
                tmp_trains = trains[:]
                coupled = trains[l1] + trains[l2][::-1]
                for i in range(len(coupled) + 1):
                    tmp_trains[l1] = coupled[:i]
                    tmp_trains[l2] = coupled[i:][::-1]
                    tmp_state = '|'.join(tmp_trains)
                    if tmp_state not in bk_rec:
                        if tmp_state in fwd_rec:
                            return fwd_rec[tmp_state] + step
                        bk_rec[tmp_state] = step
                        tmp_backward.append(tmp_trains[:])
            for l1, l2 in exch3:
                tmp_trains = trains[:]
                coupled = trains[l1][::-1] + trains[l2]
                for i in range(len(coupled) + 1):
                    tmp_trains[l1] = coupled[:i][::-1]
                    tmp_trains[l2] = coupled[i:]
                    tmp_state = '|'.join(tmp_trains)
                    if tmp_state not in bk_rec:
                        if tmp_state in fwd_rec:
                            return fwd_rec[tmp_state] + step
                        bk_rec[tmp_state] = step
                        tmp_backward.append(tmp_trains[:])
        backward = tmp_backward

def main():
    from sys import stdin
    f_i = stdin
    
    while True:
        x, y = map(int, f_i.readline().split())
        
        if x == 0:
            break
        
        print(solve(f_i, x, y))

main()
