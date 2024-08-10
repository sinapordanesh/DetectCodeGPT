n,m,k = map(int,input().split())

def hantei(n,m,k):
    for i in range(n+1):
        for j in range(m+1):
            if i*m + j*(n-2*i)==k:
                return True
    return False

print("Yes" if hantei(n,m,k) else "No")
