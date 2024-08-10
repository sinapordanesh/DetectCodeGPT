import sys
readline = sys.stdin.readline

import itertools

# DEBUG = True
DEBUG = False

N = int(readline())

class Interactive:
    def __init__(self):
        self.ques_cnt = 0
        self.create_data()
        
    def create_data(self):
        import random
        self.upper = ''.join(random.choice('.#') for _ in range(N))
        self.lower = ''.join(random.choice('.#') for _ in range(N))
        print('created upper:', self.upper)
        print('created lower:', self.lower)
        
    def resp_ques(self, *args):
        self.ques_cnt += 1
        if len(args) != 1:
            raise ValueError('不正な質問', args)
        S,T = args[0].split()
        L = len(S)
        for i in range(N):
            if S == self.lower[i:i+L] and T == self.upper[i:i+L]:
                if len(S) == N:
                    return 'end\n'
                else:
                    return 'T\n'
        return 'F\n'
            
    def resp_ans(self, *args):
        pass
            
if DEBUG:
    interactive = Interactive()
    
def question(*args, offset=None):
    if offset is None:
        print(*args, flush=True)
    else:
        print(offset, *args, flush=True)
    if DEBUG:
        resp = interactive.resp_ques(*args)
        print(resp)
        return resp
    else:
        return readline()
    
def answer(*args, offset=None):
    if offset is None:
        print(*args, flush=True)
    else:
        print(offset, *args, flush=True)
    if DEBUG:
        interactive.resp_ans(*args)
    else:
        exit()

col_patterns = tuple(itertools.product('.#', repeat=2))

def find_some_col():
    for S,T in col_patterns:
        resp = question(S + '\n' + T).rstrip()
        if resp == 'T':
            return S,T
        if resp == 'end':
            exit()

def extend_left(S,T):
    while True:
        flag = False
        for s,t in col_patterns:
            resp = question(s + S + '\n' + t + T).rstrip()
            if resp == 'T':
                flag = True
                S = s + S
                T = t + T
                break
            elif resp == 'end':
                exit()
        if not flag:
            return S,T

def extend_right(S,T):
    while True:
        flag = False
        for s,t in col_patterns:
            resp = question(S + s + '\n' + T + t).rstrip()
            if resp == 'T':
                flag = True
                S = S + s
                T = T + t
                break
            elif resp == 'end':
                exit()
        if not flag:
            return S,T

S,T = find_some_col()
S,T = extend_left(S,T)
S,T = extend_right(S,T)