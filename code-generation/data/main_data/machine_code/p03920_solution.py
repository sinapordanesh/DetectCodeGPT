def solve_problem():
    N = int(input())
    ans = []
    for i in range(1, N+1):
        if N - i > i:
            ans.append(i)
            N -= i
    for i in ans:
        print(i)