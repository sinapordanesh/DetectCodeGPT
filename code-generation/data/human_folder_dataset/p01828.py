def f(s,t):
    j=0;i=0
    while i<len(t) and j<len(s):
        if t[i]==s[j]:j+=2
        i+=1
    return j>=len(s)
I=input
s=I()
t=I()
print(['No','Yes'][f(s,t) or f(s[1:],t)])