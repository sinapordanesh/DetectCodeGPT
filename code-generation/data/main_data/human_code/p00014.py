def get_input():
    while True:
        try:
            yield int(raw_input())
        except EOFError:
            break

num_lis = list(get_input())

for num in num_lis:
    all_count = 600/num
    S = 0
    for i in range(all_count-1):
        count = i+1
        yoko = num
        tate = (count*num)**2
        S += (yoko*tate)
    print(S)