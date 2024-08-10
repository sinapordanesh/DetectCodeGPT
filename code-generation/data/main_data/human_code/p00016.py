# -*- coding:utf-8 -*-

def main():
    import math
    LIST=[0,0,math.radians(90)]
    while True:
        a,b=map(float,input().split(","))
        if a==0 and b==0:
            break
        else:
            b=math.radians(b)
            LIST[0]+=a*math.sin(LIST[2])
            LIST[1]+=a*math.cos(LIST[2])
            LIST[2]-=b

    print(int(LIST[1]))
    print(int(LIST[0]))
    
if __name__ == '__main__':
    main()