
max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

N,M = map(int,input().split())
A = tuple(map(lambda x:int(x)-1,input().split()))

A = [a for a,b in zip(A,A[1:]) if a != b]+[A[-1]]


def it():
    events = [(a+1,-1) for a in A[:-1]] + [(a,p+1) for p,a in zip(A,A[1:])]
    events.sort()
    discount = 0
    cnt = 0
    for a,b in zip(A,A[1:]):
        discount += max2(0, (b-a)%M - 1 - b)
        cnt += int(b < a)
    yield discount
    last = 0
    for a,p in events:
        discount += (a-last)*cnt
        yield discount
        if p < 0:
            cnt += 1
        else:
            cnt -= 1
            discount -= (a-p)%M
        last = a

    yield discount

total = sum((b-a)%M for a,b in zip(A,A[1:]))
print(total - max(it()))