def main():
    a, b = map(int, input().split())
    
    h = ((max(a, b) - 1) // 16 + 1) * 3
    w = 96 # 3 * 32

    print(h, w)

    ans = []
    line1 = ['.', '.', '.', '#', '#', '#'] * 16
    line2 = ['#', '#', '#', '.', '.', '.'] * 16

    for i in range(h//3):
        if i % 2 == 0:
            ans.append(line1.copy())
            ans.append(line1.copy())
            ans.append(line1.copy())
        else:
            ans.append(line2.copy())
            ans.append(line2.copy())
            ans.append(line2.copy())

    if a <= b:
        a, b = b, a
        flag = True
    else:
        flag = False

    if a % 16 > 0:
        for i in range(6 * (16 - a % 16) + 3):
            ans[-1][i] = '.'

    if h == 3:
        for i in range(6 * (16 - b) + 3):
            ans[0][i] = '#'
    else:
        num = h//3 * 16 - b
        for i in range(num // 16):
            if ans[2 + 3*i][0] == '.':
                for j in range(16):
                    ans[2 + 3*i][2 + 6*j] = '#'
            else:
                for j in range(16):
                    ans[2 + 3*i][3 + 6*j] = '#'

        if ans[-3][0] == '.':
            for i in range(num % 16):
                ans[-3][6 + 6*i] = '#'
        else:
            for i in range(num % 16):
                ans[-3][5 + 6*i] = '#'

    if flag:
        for i in range(h):
            for j in range(w):
                if ans[i][j] == '.':
                    ans[i][j] = '#'
                else:
                    ans[i][j] = '.'

    for i in ans:
        print(''.join(i))

main()