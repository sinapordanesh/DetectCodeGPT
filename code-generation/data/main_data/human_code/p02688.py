import math
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]

mnum,snum=i_map()
snholder=set()
for i in range(snum):
    d=i_input()
    ls=i_list()
    snholder=snholder | set(ls)
print(mnum-len(snholder))

