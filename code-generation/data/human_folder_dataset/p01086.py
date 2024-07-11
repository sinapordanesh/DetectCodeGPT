ans_list = []

def make_tanka(num, w_list, i):
    #print(num, w_list, i)
    cnt = 0
    while cnt < num:
        cnt += len(w_list[i])
        i += 1
    return [cnt, i]

while True:
    n = int(input())
    if n == 0:
        break
    w_list = []
    for i in range(n):
        w_list.append(input())

    f1 = 0
    s1 = 0
    f2 = 0
    s2 = 0
    s3 = 0
    i = 0
    ans = -1
    while True:
        #print(i)
        j = i
        f1, j = make_tanka(5, w_list, j)
        if f1 == 5:
            s1, j = make_tanka(7, w_list, j)
            if s1 == 7:
                f2, j = make_tanka(5, w_list, j)
                if f2 == 5:
                    s2, j = make_tanka(7, w_list, j)
                    if s2 == 7:
                        s3, j = make_tanka(7, w_list, j)
                        if s3 == 7:
                            ans = i
                            break
                    if ans != -1:
                        break
                if ans != -1:
                    break
            if ans != -1:
                break
        if ans != -1:
            break
        i += 1
    ans_list.append(ans + 1)

for i in ans_list:
    print(i)
