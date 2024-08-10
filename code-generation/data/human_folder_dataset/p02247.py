#coding:utf-8

def NSS(s1,s2):
    s1list=list(s1)
    n=len(s1list)
    s2list=list(s2)
    for i in range(n):
        ans=0
        if len(s1list)>=len(s2list) and s1list[0]==s2list[0]:
            ans+=1
            for j in range(1,len(s2list)):
                if s1list[j]==s2list[j]:
                    ans+=1
        if ans==len(s2list):
            print(i)
        s1list.pop(0)

if __name__=="__main__":
    s1=input()
    s2=input()
    NSS(s1,s2)
        
            