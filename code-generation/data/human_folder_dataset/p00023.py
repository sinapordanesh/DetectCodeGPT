# -*- coding:utf-8 -*-

def main():
    import math
    for i in range(int(input())):
        xa,ya,ra,xb,yb,rb=map(float,input().split())
        d=math.sqrt((xa-xb)**2+(ya-yb)**2)
        if d>ra+rb:
            print(0)

        elif ra+rb>=d and d>=abs(ra-rb):
            print(1)

        elif d<abs(ra-rb):
            if ra>rb:
                print(2)
            elif ra<rb:
                print(-2)
        
            
    
        
if __name__ == '__main__':
    main()