N = int(input())
A = [(int(x), i+1) for i, x in enumerate(input().split())]

def test(N, A):
    answer = 0
    for a0, i0 in A:
        for a1, i1 in A:
            if a1 + a0 == abs(i1 - i0):
                answer += 1
    return answer // 2

def solve(N, A):
    memo0 = {}
    memo1 = {}
    for a, n in A:
        k = - (a+n)
        if k not in memo0:
            memo0[k] = 0
        memo0[k]+=1
        k = n-a
        if k not in memo1:
            memo1[k] = 0
        memo1[k]+=1
    #print(f"{memo0=}")
    #print(f"{memo1=}")
    answer = 0
    for a, n in A:
        k = a - n
        if k in memo0:
            answer += memo0[k]
        k = a + n
        if k in memo1:
            answer += memo1[k]

    return answer // 2

#print(test(N, A))
print(solve(N, A))


