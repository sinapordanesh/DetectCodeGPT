# 要素が入ってない場合の list.index の定義
def myindex(l:list, element, default=-1):
    if element in set(l):
        return l.index(element)
    else:
        return default

def main():
    n = int(input())
    S = []
    ans = ''
    for _ in range(n):
        S.append(list(input()))
    
    S.sort()
    t = S.pop()
    for i, u in enumerate(t):
        okflag = True
        for s in S:
            if myindex(s, u) == -1:
                okflag = False
                break
        if okflag:
            for s in S:
                s.pop(s.index(u))
            ans += u
    ans = sorted(ans)
    print(''.join(ans))

if __name__ == "__main__":
    main()
