import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B, C = mapint()
costs = {'A': A, 'B': B, 'C': C}
old_a, old_b = list(input())

if costs[old_a]==0 and costs[old_b]==0:
    print('No')
    exit()

commands = []
for _ in range(N-1):
    nx_a, nx_b = list(input())
    if costs[old_a]==0 and costs[old_b]==0:
        print('No')
        exit()
    elif costs[old_a]==0:
        costs[old_a] += 1
        costs[old_b] -= 1
        commands.append(old_a)
        
    elif costs[old_b]==0:
        costs[old_b] += 1
        costs[old_a] -= 1
        commands.append(old_b)

    else:
        if old_a==nx_a or old_a==nx_b:
            commands.append(old_a)
            costs[old_a] += 1
            costs[old_b] -= 1
        else:
            commands.append(old_b)
            costs[old_b] += 1
            costs[old_a] -= 1
    old_a, old_b = nx_a, nx_b

if costs[old_a]==0 and costs[old_b]==0:
    print('No')
    exit()
elif costs[old_a]==0:
    costs[old_a] += 1
    costs[old_b] -= 1
    commands.append(old_a)
    
else:
    costs[old_b] += 1
    costs[old_a] -= 1
    commands.append(old_b)

print('Yes')
print('\n'.join(commands))