
from collections import defaultdict

def main():
    num, k = map(int, input().split())
    data = [input() for i in range(num)]
    initial_dic = defaultdict(int)
    for i in range(num):
        initial_dic[data[i][0]] += 1

    aaa = list(initial_dic.values())
    aaa.sort(reverse=True)
    ans = 0
    if len(aaa) < k:
        pass
    else:
        while 1:
            if aaa[k - 1] == 0:
                break
            for i in range(k):
                aaa[i] -= 1
            ans += 1
            aaa.sort(reverse=True)

    print(ans)




if __name__ == '__main__':
    main()