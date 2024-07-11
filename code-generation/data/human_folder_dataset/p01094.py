def ri(): return int(input())
cand = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()

n = ri()
while(n!=0):
    vote = input().split()
    sm = [0 for i in range(26)]
    flag = False
    for i in range(n):
        for j in range(26):
            if(vote[i] == cand[j]):
                sm[j] += 1
                break
        no1_sm = 0
        no2_sm = 0
        no1_idx = 0
        no2_idx = 0
        for j in range(26):
            if(sm[j] > no1_sm):
                no2_sm = no1_sm
                no2_idx = no1_idx
                no1_sm = sm[j]
                no1_idx = j
            elif(sm[j] > no2_sm):
                no2_sm = sm[j]
                no2_idx = j
        if((i+1) > n//2 and no1_sm > no2_sm+(n-1-i)):
            print(cand[no1_idx], i+1)
            flag = True
            break
        if(flag): break
    if(not flag):
        print("TIE")
    n = ri()