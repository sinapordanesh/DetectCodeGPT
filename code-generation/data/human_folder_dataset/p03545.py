a,b,c, d = [ int(i) for i in list(input()) ]



def calc(x,y,op):
    if op == '+':
        return x+y
    else:
        return x-y


op_l = ['+','-']
for op1 in op_l:
    for op2 in op_l:
        for op3 in op_l:
            x = calc(calc(calc(a,b,op1),c,op2),d, op3)
            if x == 7:
                ans = str(a)+op1+str(b)+op2+str(c)+op3+str(d)+"=7"
                break
print(ans)