import sys
import bisect
input = sys.stdin.readline

def cumsum(inlist):
    s = 0
    outlist = []
    for i in inlist:
        s += i
        outlist.append(s)
    return outlist
    
oneday = 86400 
time = [ 0 for i in range(oneday) ]
n = int(input())
t = 0
for i in range(n):
    a, b = [ int(v) for v in input().split() ]
    t = (t+a) % oneday
    time[t] += 1
    t = (t+b) % oneday

time = time * 2
timesum = cumsum(time)

ans_list = []
for i in range(oneday*2-20000):
    ans_list.append(timesum[i+10801] - timesum[i])
print(max(ans_list))
