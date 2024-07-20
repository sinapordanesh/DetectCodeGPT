# -*- coding:utf-8 -*-

def main():
    LIST=[]

    while True:
        try:
            N=int(input())
            flag=True
            for item in LIST:
                if item[0]==N:
                    index=LIST.index(item)
                    flag=False

            if flag:
                LIST.append([N,1])
            else:
                LIST[index][1]+=1


        except:
            break
    m=0
    for i in LIST:
        m=max(m,i[1])
    ans=sorted([x for x in LIST if x[1]==m],key=lambda x:x[0])
    for i in ans:
        print(i[0])

    
if __name__ == '__main__':
    main()