def sol(h,w):
    d = (h*h) + (w*w)
    ans =(150,150)
    for dw in range(1,150):
        for dh  in range(1,dw):
            dd = (dw*dw) +  (dh*dh)
            if dd < d:continue
            if dw == w and dh == h:continue
            if dd == d and dh < h:continue
            da = (ans[0]*ans[0]) + (ans[1]*ans[1])
            if dd < da:ans = (dh,dw)
            elif dd == da:
                if dh < ans[0]: ans = (dh,dw)
    print(*ans)

if __name__ =="__main__":       
    while 1:
        h,w = list(map(int,input().split(' ')))
        if h ==0:break
        sol(h,w)
