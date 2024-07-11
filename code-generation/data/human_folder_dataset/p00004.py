def equation(a,b,c,d,e,f,x):
    buff = a*e-b*d
    buff_a = a

    a = e/buff
    b = -b/buff
    d = -d/buff
    e = buff_a/buff

    x.append((a*c)+(b*f))
    x.append((d*c)+(e*f))

count = 0
a = []
b = []
c = []
d = []
e = []
f = []

while True:
    try:
        buff = input().split()
        a.append(float(buff[0]))
        b.append(float(buff[1]))
        c.append(float(buff[2]))  
        d.append(float(buff[3]))
        e.append(float(buff[4]))
        f.append(float(buff[5]))
        count += 1
    except:
        break

for i in range(count):
    ans = []

    equation(a[i],b[i],c[i],d[i],e[i],f[i],ans)
    print('{:.3f}'.format(ans[0]),'{:.3f}'.format(ans[1]))
