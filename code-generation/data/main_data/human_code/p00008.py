def count(num):    
    l1=[]
    for a in range (10):
        for b in range(10):
            for c in range (10):
                for d in range (10):
                    l1.append([a,b,c,d])
    l1=list(filter(lambda x: sum(x)==num,l1))
    return(len(l1))

while True:
    try:
        print(count(int(input())))
    except:
        break
    