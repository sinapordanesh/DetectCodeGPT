max_size = 0

def get_max_rectangle(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                max_rectangle_right(field, {'x0':j, 'y0':i, 'x1':j, 'y1':i})

def check_expandable(field, rect, a0, a1, b, c):
    return rect[a1] - rect[a0] + 1 == len([i for i in range(rect[a0], rect[a1]+1) if field[rect[b]+c][i] == 1])

def check_fill_ones(field, rect):
    for i in range(rect['x0'], rect['x1']+1):
        for j in range(rect['y0'], rect['y1']+1):
            if field[j][i] == 0:
                return False
    return True

def max_rectangle_right(field, rect):
    #右拡張
    if rect['y1'] - rect['y0'] + 1 == len([i for i in range(rect['y0'], rect['y1']+1) if field[i][rect['x1']+1] == 1]):
        tmp_rect = dict(rect)
        tmp_rect['x1'] += 1
        max_rectangle_right(field, tmp_rect)

    #下拡張
    if rect['x1'] - rect['x0'] + 1 == len([i for i in range(rect['x0'], rect['x1']+1) if field[rect['y1']+1][i] == 1]):
        tmp_rect = dict(rect)
        tmp_rect['y1'] += 1
        max_rectangle_right(field, tmp_rect)

    global max_size
    if check_fill_ones(field, rect):
        max_size = max(max_size, (rect['x1']-rect['x0']+1) * (rect['y1']-rect['y0']+1))

def input_field(y, x):
    field = []
    for i in range(y):
        field.append(map(int, raw_input().split()))
    return pack_field(field, y, x)

def pack_field(field, y, x):
    packed_field = []
    for i in range(y + 2):
        packed_field.append([])
        if i == 0 or i == y + 1:
            for j in range(x + 2):
                packed_field[i].append(0)
        else:
            packed_field[i].append(0)
            for j in range(x):
                packed_field[i].append(field[i-1][j])
            packed_field[i].append(0)
    return packed_field

maxs = []
num = int(raw_input())
first = True
for i in range(num):
    if not first:
        raw_input()

    max_size = 0
    field = input_field(5, 5)
    get_max_rectangle(field)
    maxs.append(max_size)
    first = False

for i in range(num):
    print(maxs[i])