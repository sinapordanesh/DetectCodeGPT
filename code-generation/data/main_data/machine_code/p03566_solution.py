def atcoder_express(N, t, v):
    t = [0] + t + [0]
    for i in range(1, N+2):
        t[i] += t[i-1]
    total = sum(t)
    v = [0] + v + [0]
    for i in range(1, N+2):
        v[i] = min(v[i], v[i-1] + 1)
    ans = 0
    for i in range(total*2):
        time = min(i//2, total-i//2)
        dist = 0
        for j in range(1, N+2):
            left = max(0, time-t[j-1])
            right = max(0, t[j]-time)
            if left < right:
                dist += min(v[j-1]+left, v[j-1]+right*(v[j]-v[j-1])/(t[j]-t[j-1])-right)
            else:
                dist += min(v[j]+right, v[j-1]+left*(v[j]-v[j-1])/(t[j]-t[j-1])-left)
        ans = max(ans, dist)
    return ans

# Test the function with sample inputs
print(atcoder_express(1, [100], [30]))
print(atcoder_express(2, [60, 50], [34, 38]))
print(atcoder_express(3, [12, 14, 2], [6, 2, 7]))
print(atcoder_express(1, [9], [10]))
print(atcoder_express(10, [64, 55, 27, 35, 76, 119, 7, 18, 49, 100], [29, 19, 31, 39, 27, 48, 41, 87, 55, 70]))