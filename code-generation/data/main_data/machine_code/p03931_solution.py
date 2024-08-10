def count_patterns(n, m, arr):
    MOD = 1000000007
    
    def comb(n, r):
        if r == 0 or n == r:
            return 1
        return (fact[n] * pow(fact[r], MOD-2, MOD) * pow(fact[n-r], MOD-2, MOD)) % MOD

    fact = [1] * (n+1)
    for i in range(2, n+1):
        fact[i] = (fact[i-1] * i) % MOD

    arr.sort()
    ans = 1
    for i in range(n):
        ans = (ans * comb(m-1, arr[i]-1)) % MOD
        m -= arr[i]

    return ans

# Sample Input 1
n1 = 3
m1 = 1
arr1 = [1, 2, 3]
print(count_patterns(n1, m1, arr1))

# Sample Input 2
n2 = 3
m2 = 10
arr2 = [8, 7, 5]
print(count_patterns(n2, m2, arr2))

# Sample Input 3
n3 = 25
m3 = 127
arr3 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
print(count_patterns(n3, m3, arr3))