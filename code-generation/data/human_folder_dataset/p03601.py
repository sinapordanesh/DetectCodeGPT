A,B,C,D,E,F = map(int,input().split())
Ans = [0,100*A,0]
def Con(water,sugar):
    return 100*(sugar)/(water+sugar)
def limit(water):
    return water*E//100
for NumA in range(1,F//(100*A)+2):
    for NumB in range(0,F//(100*B)+1):
        water = 100*(A*NumA+B*NumB)
        lim1 = limit(water)
        lim2 = F-water
        lim = min(lim1,lim2)
        for i in range(lim//D+1):
            sugar = D*i
            sugar += ((lim-sugar)//C)*C
            Con1 = Con(water,sugar)
            if Ans[0] < Con1:
                Ans = [Con1,water,sugar]
print(Ans[1]+Ans[2],Ans[2])