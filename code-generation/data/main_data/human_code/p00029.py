# -*- coding:utf-8 -*-

def main():
    LIST=[]

    while True:
        try:
            val=input().split()
            LIST=[]
            
            
            for v in val:
                flag=True
                for item in LIST:
                    if item[0]==v:
                        index=LIST.index(item)
                        flag=False

                if flag:
                    LIST.append([v,1])
                else:
                    LIST[index][1]+=1

            longest=""
            LIST=sorted(LIST,key=lambda x:x[1],reverse=True)
            for i in LIST:
                longest=i[0] if max(len(longest),len(i[0]))==len(i[0]) else longest

                
            ans=LIST[0][0]
            print("{0} {1}".format(ans,longest))

        except:
            break

    
if __name__ == '__main__':
    main()