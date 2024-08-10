import re

def get_value(expr, array_size, array):
    seq = expr.replace(']', '').split('[')
    seq[-1] = int(seq[-1])
    while len(seq) > 1:
        ind = seq.pop()
        arr = seq.pop()
        if arr not in array or ind not in array[arr]:
            raise KeyError

        seq.append(array[arr][ind])

    return seq[0]

def testcase_ends():
    array_size = {}
    array = {}

    decl_prog = re.compile(r'(\w)\[(\d+)\]')

    line = input().strip()
    if line == '.':
        return True

    i = 1
    while True:
        if line == '.':
            print(0)
            return False

        if '=' in line:
            # assignment
            lhs, rhs = line.split('=')

            name = lhs[0]
            try:
                ind = get_value(lhs[2:-1], array_size, array)
                value = get_value(rhs, array_size, array)
                if name not in array or ind >= array_size[name]:
                    raise KeyError

                array[name][ind] = value
            except KeyError:
                print(i)
                break
        else:
            # declaration
            m = decl_prog.fullmatch(line)
            assert m is not None

            name = m.group(1)
            size = int(m.group(2))
            array_size[name] = size
            array[name] = {}

        line = input().strip()
        i += 1

    line = input().strip()
    while line != '.':
        line = input().strip()

    return False

while not testcase_ends():
    pass

