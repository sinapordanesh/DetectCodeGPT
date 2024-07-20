import sys

def hitBlow(a, b):
    hit = 0
    blow = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            hit += 1
        else:
            for j in range(len(b)):
                if a[i] == b[j]:
                    blow += 1

    return [hit, blow]

for s in sys.stdin:
    a = list(map(int, s.split()))
    b = list(map(int, input().split()))

    hit, blow = hitBlow(a, b)

    print(hit, blow)