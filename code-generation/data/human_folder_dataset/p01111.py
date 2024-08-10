import sys

def resolve(buget,num):
    return ((((2*buget)/num)-num+1)/2)

for buget in sys.stdin:
    buget = int(buget)
    if buget == 0 :
        break

    num = 1
    answer_floor = 1
    answer_num = 1
    answer = 0
    while (num*num)/2 < buget :
        #num を増やしていって、aの解が整数になるかをチェックする
        answer = resolve(buget,num)
        if answer.is_integer():
            answer_floor = answer
            answer_num = num
        num = num + 1
    print(str(int(answer_floor)) + " " + str(answer_num))

