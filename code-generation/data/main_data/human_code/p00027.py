# -*- coding:utf-8 -*-

def main():
    LIST=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    while True:
        try:
            count=3
            M,D=map(int,input().split())
            if M==0:
                break

            if M in [1,4,7]:
                pass
            elif M in [10]:
                count+=1
            elif M in [5]:
                count+=2
            elif M in [2,8]:
                count+=3
            elif M in [3,11]:
                count+=4
            elif M in [6]:
                count+=5
            elif M in [9,12]:
                count+=6

            count+=D%7

            print(LIST[count%7])

        except:
            break

if __name__ == '__main__':
    main()