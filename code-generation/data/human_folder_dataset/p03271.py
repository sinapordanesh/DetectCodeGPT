import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
P = [0] + list(map(int,read().split()))

# permutationになっている極小区間に分ける

intervals = []
left = 0
right = -1
for i,p in enumerate(P):
    if right < p:
        right = p
    if i == right:
        intervals.append((left,right))
        left = i+1
        right = -1

def check(L,R):
    if L == R:
        return True
    to_left = []
    fixed = []
    to_right = []
    for i,p in enumerate(P[L:R+1],L):
        if i > p:
            to_left.append(p)
        elif i == p:
            fixed.append(p)
        else:
            to_right.append(p)
            
    if fixed != list(range(L+1,R+1,2)):
        return False
    if any(x > y for x,y in zip(to_left, to_left[1:])):
        return False
    if any(x > y for x,y in zip(to_right, to_right[1:])):
        return False
    return True

answer = 'Yes' if all(check(L,R) for L,R in intervals) else 'No'
print(answer)