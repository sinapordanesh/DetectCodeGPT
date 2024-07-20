def rotateX(dice):
    d1, d2, d3, d4, d5, d6 = dice
    return [d2, d6, d3, d4, d1, d5]


def rotateY(dice):
    d1, d2, d3, d4, d5, d6 = dice
    return [d4, d2, d1, d6, d5, d3]


def rotateZ(dice):
    d1, d2, d3, d4, d5, d6 = dice
    return [d1, d3, d5, d2, d4, d6]


def check():
    global n, s_count
    diff = [[0 for i in range(s_count)] for j in range(6)]
    for dice in color_list[:-1]:
        for i in range(6):
            if color_list[-1][i] != dice[i]:
                diff[i][dice[i]] += 1
    count = 0

    for c in diff:
        c_max = max(c)
        c_sum = sum(c)
        if n - c_max < c_sum:
            count += n - c_max
        else:
            count += c_sum

    return count


def solve(i):
    global ans
    if i == len(color_list) - 1:
        count = check()
        if ans > count:
            ans = count
    else:
        dice_memo = []
        for x in range(4):
            temp_dice = rotateX(color_list[i])
            for y in range(4):
                temp_dice = rotateY(temp_dice)
                for z in range(4):
                    temp_dice = rotateZ(temp_dice)
                    color_list[i] = temp_dice
                    if color_list[i] in dice_memo:
                        continue
                    dice_memo.append(color_list[i])
                    solve(i + 1)


while True:
    n = int(input())
    if n == 0:
        break

    memo = {}
    s_count = 0
    color_list = [[0 for j in range(6)] for i in range(n)]
    for i in range(n):
        for j, s in enumerate(input().split(" ")):
            if s not in memo:
                color_list[i][j] = memo.setdefault(s, s_count)
                s_count += 1
            else:
                color_list[i][j] = memo[s]

    if n == 1:
        print(0)
        continue
    ans = float("inf")
    solve(0)
    print(ans)

