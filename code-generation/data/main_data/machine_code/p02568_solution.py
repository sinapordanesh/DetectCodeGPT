def process_queries(N, Q, array, queries):
    a = array
    MOD = 998244353
    ans = []
    
    for q in queries:
        if q[0] == 0:
            l, r, b, c = q[1], q[2], q[3], q[4]
            for i in range(l, r):
                a[i] = (b * a[i] + c) % MOD
        else:
            l, r = q[1], q[2]
            ans.append(sum(a[l:r]) % MOD)
    
    return ans

# Sample Input
N = 5
Q = 7
array = [1, 2, 3, 4, 5]
queries = [[1, 0, 5],
           [0, 2, 4, 100, 101],
           [1, 0, 3],
           [0, 1, 3, 102, 103],
           [1, 2, 5],
           [0, 2, 5, 104, 105],
           [1, 0, 5]]

output = process_queries(N, Q, array, queries)
for ans in output:
    print(ans)