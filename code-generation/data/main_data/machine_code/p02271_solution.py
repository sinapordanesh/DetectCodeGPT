def can_make_sum(n, arr, q, queries):
    def solve(p, t):
        if t == 0:
            return True
        if p >= n or t < 0:
            return False
        return solve(p+1, t-arr[p]) or solve(p+1, t)
    
    for query in queries:
        if solve(0, query):
            print("yes")
        else:
            print("no")

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = list(map(int, input().split()))

can_make_sum(n, arr, q, queries)