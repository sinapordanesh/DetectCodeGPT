import string
from heapq import heapify, heappop, heappush


def judge():
    import Levenshtein
    import subprocess

    ans = 'OQqZbgyIYiB59fqHVsXu0PZVEWy1sApStRxCJFMeNkr5O0U4jEX9ksBTpKw7Z3ylYd3Hnd'
    query_count = 0
    with subprocess.Popen(['python', __file__, 'EXE'],
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as p:
        while True:
            query = p.stdout.readline().decode().strip()
            print(query)
            if query[0] == '?':
                d = Levenshtein.distance(query[2:], ans)
                print(d)
                p.stdin.write(f'{d}\n'.encode())
                p.stdin.flush()
                query_count += 1
            elif query[0] == '!':
                print(query[2:] == ans)
                print(query_count)
                break
            else:
                pass


# import sys
#
# if len(sys.argv) == 1:
#     print('Interactive Test Mode')
#     judge()
#     exit()

STR = string.ascii_letters + string.digits
counter = {}
for c in STR:
    print(f'? {c * 128}')
    a = int(input())
    if a == 128:
        continue
    counter[c] = 128 - a

l = sum(counter.values())
q = [(cnt, [c] * cnt) for c, cnt in counter.items()]
heapify(q)

while len(q) > 1:
    l1, t1 = heappop(q)
    l2, t2 = heappop(q)
    i = 0
    j = 0
    while i < len(t1) and j < l2:
        t1.insert(i, t2[j])
        s = ''.join(t1)
        print(f'? {s}')
        a = int(input())
        if len(t1) > l - a:
            t1.pop(i)
        else:
            j += 1
        i += 1
    if j < len(t2):
        t1.extend(t2[j:])

    heappush(q, (l1 + l2, t1))

_, t = q[0]
s = ''.join(t)
print(f'! {s}')
