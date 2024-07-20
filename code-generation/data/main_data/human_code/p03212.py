N=int(input())
L=[3, 5, 7]
 
def dfs(s):
    if s>N:
        return False
 
    str_s = str(s)
    return sum(dfs(s*10 + i) for i in L) + ("7" in str_s and "5" in str_s and "3" in str_s)
 
 
print(dfs(0))