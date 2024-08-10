# 実際に判定を行う
def solve(key1, key2):
    key2 = Normalization(key2)
    for _ in range(4):
        key1 = x_rotate(key1)
        for __ in range(4):
            key1 = y_rotate(key1)
            for ___ in range(4):
                key1 = z_rotate(key1)
                ans = True
                for line in key2:
                    if line not in key1 and [line[1], line[0]] not in key1:
                        ans = False
                if ans:
                    return True
    return False

def x_rotate(key):
    tmpkey = []
    for pos in key:
        tmppos = []
        for i in pos:
            tmppos.append([i[0], i[2], -i[1]])
        tmpkey.append(tmppos)

    return Normalization(tmpkey)

def y_rotate(key):
    tmpkey = []
    for pos in key:
        tmppos = []
        for i in pos:
            tmppos.append([-i[2], i[1], i[0]])
        tmpkey.append(tmppos)

    return Normalization(tmpkey)

def z_rotate(key):
    tmpkey = []
    for pos in key:
        tmppos = []
        for i in pos:
            tmppos.append([i[1], -i[0], i[2]])
        tmpkey.append(tmppos)

    return Normalization(tmpkey)


# +xとかの判定
def check_pn_xyz(pn_xyz):
    if pn_xyz[0]== '+':
        if pn_xyz[1] == 'x':
            return [1, 0, 0]
        elif pn_xyz[1] == 'y':
            return [0, 1, 0]
        else:
            return [0, 0, 1]
    else:
        if pn_xyz[1] == 'x':
            return [-1, 0, 0]
        elif pn_xyz[1] == 'y':
            return [0, -1, 0]
        else:
            return [0, 0, -1]

# 同じ長さのリスト同士の足し算
def add(lista, listb):
    ret = []
    for i in range(len(lista)):
        ret += [lista[i] + listb[i]]
    return ret

# 鍵を正規化する (基準を[0, 0, 0]に)
def Normalization(key):
    x, y, z = float('inf'), float('inf'), float('inf')
    for pos in key:
        for i in pos:
            x, y, z = min(x, i[0]), min(y, i[1]), min(z, i[2])
    tmpkey = []

    for pos in key:
        tmppos = []
        for i in pos:
            tmppos.append([i[0] - x, i[1] - y, i[2] - z])
        tmpkey.append(tmppos)
    return tmpkey

# こっからメイン
past_key, now_key = [], []
while True:
    # 入力とか
    isneed_input = True
    if not past_key:
        past_key, now_key, i = now_key, [], 0
    else:
        past_key, now_key, i = [], [], 0
    makekey_pos, now_pos = {'0': (0, 0, 0)}, [0, 0, 0]
    N = False
    while not N:
        N = input()

    # 1行に集約されていた場合
    if not N.isdecimal():
        N, *string = N.split()
        isneed_input = False

    N = int(N)
    if not N:
        break

    # 鍵の部分の入力
    while i < N:
        if isneed_input:
            string = input().split()  # stringという名称だがlist, 命名ミス
        for num in range(len(string)):
            if string[num].isdecimal():
                if string[num] not in makekey_pos.keys():
                    makekey_pos[string[num]] = now_pos
                else:
                    now_pos = makekey_pos[string[num]]
            else:
                now_key.append([now_pos])
                now_pos = add(check_pn_xyz(string[num]), now_pos)
                now_key[-1].append(now_pos)
            i += 1

    # 一個前のやつと比較
    if past_key:
        print('SAME' if solve(now_key, past_key) else 'DIFFERENT')

