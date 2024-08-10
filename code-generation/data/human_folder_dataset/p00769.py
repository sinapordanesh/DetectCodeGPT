def rec(s):
    ans = int(1e8)
    c_list = []
    st = []
    n = len(s)
    l = 0
    r = len(s)-1
    if s[0]!='[':
        return 1+int(s)//2
    for i in range(n):
        _s = s[i]
        if _s=='[':
            if len(st)==0:
                l = i+1
            st.append(_s)
        elif _s==']':
            st = st[:-1]
            if len(st)==0:
                r = i
                c_list.append(rec(s[l:r]))
    c_list.sort()
    return sum( c_list[:1+len(c_list)//2] )

N = int(input())
for _ in range(N):
    s = input()
    print(rec(s))