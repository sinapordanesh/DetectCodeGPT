def A():
    s = input()
    if s == 'SSS': print(3)
    elif s=='RSS' or s=='SSR': print(2)
    elif s=='RRR': print(0)
    else: print(1)

def B():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]: continue
            for k in range(j+1, n):
                if a[i]==a[k] or a[j] == a[k]: continue
                s = a[i] + a[j] + a[k]
                if s > 2 * max(a[i], a[j], a[k]):
                    cnt += 1
    print(cnt)

def C():
    x, k, d = map(int, input().split())
    if abs(x) > k * d:
        print(abs(x) - k*d)
    else:
        tm = abs(x) // d
        x = abs(x) % d
        k -= tm
        if k % 2 == 0:
            print(x)
        else:
            print(d-x)
B()
