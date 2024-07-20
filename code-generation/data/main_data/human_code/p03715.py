def main():
    h,w = map(int,input().split())
    #縦3分割
    h1 = h//3
    h2 = (h-h1)//2
    h3 = h-h1-h2
    ans = (max(h1,h2,h3)-min(h1,h2,h3))*w
    #横3分割
    w1 = w//3
    w2 = (w-w1)//2
    w3 = w-w1-w2
    a = (max(w1,w2,w3)-min(w1,w2,w3))*h
    if a<ans:
        ans = a
    #縦1横２分割
    h1 = h//3
    h2 = h-h1
    w1 = w//2
    w2 = w-w1
    a = max(h1*w,h2*w1,h2*w2)-min(h1*w,h2*w1,h2*w2)
    if a<ans:
        ans = a
    h1 = h//3+1
    h2 = h-h1
    w1 = w//2
    w2 = w-w1
    a = max(h1*w,h2*w1,h2*w2)-min(h1*w,h2*w1,h2*w2)
    if a<ans:
        ans = a
    #縦2横1分割
    w1 = w//3
    w2 = w-w1
    h1 = h//2
    h2 = h-h1
    a = max(w1*h,w2*h1,w2*h2)-min(w1*h,w2*h1,w2*h2)
    if a<ans:
        ans = a
    w1 = w//3+1
    w2 = w-w1
    h1 = h//2
    h2 = h-h1
    a = max(w1*h,w2*h1,w2*h2)-min(w1*h,w2*h1,w2*h2)
    if a<ans:
        ans = a
    
    print(ans)

if __name__ == "__main__":
    main()
