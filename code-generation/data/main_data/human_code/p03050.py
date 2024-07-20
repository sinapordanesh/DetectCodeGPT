n = int(input())

def make_divisors(n):
    from collections import deque
    divisors = deque([])
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    lst_divisors = list(divisors)
    lst_divisors.sort()
    return lst_divisors

lst = make_divisors(n)

#g = (n//m)*m + (n//m)
#g = (n//m)*(m+1)

ans = 0
for y in lst:
    if y > 1 and n//(y-1) == n%(y-1):
        ans += y-1
        
print(ans)