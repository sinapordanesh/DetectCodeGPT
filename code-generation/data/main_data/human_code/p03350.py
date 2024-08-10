import sys
import numpy as np

def offset(length):
    return 1 << length

def solve():
    n, k = map(int, sys.stdin.buffer.readline().split())
    buf = b"0" + sys.stdin.buffer.read().replace(b"\n", b"")
    table = (np.frombuffer(buf, dtype=np.int8).astype(np.int32) - ord(b"0"))

    offset_table = np.ones(len(table) // 2, dtype=np.int32)
    for v in range(n - 1):
        offset_table[1 << v:2 << v] = 2 << v

    ret = None
    for pos in range(n + 1):
        for length in range(pos + 1, n + 1):
            subtable = table[offset(length):offset(length + 1)]
            table[offset(pos):offset(pos + 1)] += subtable.reshape(-1, 1 << pos, order="F").sum(axis=0)
        count_table = table[offset(pos):offset(pos + 1)]
        index = np.argmax(count_table >= k)
        if count_table[index] >= k: ret = (index, pos)
        else: return ret

        for length in range(pos + 1, n + 1):
            size = 1 << length
            rest = length - pos
            half_period = 1 << (rest - 1)
            trans_table = np.arange(half_period + size, half_period + size * 2, dtype=np.int32) >> rest

            trans_reshaped = trans_table.reshape(-1, half_period * 2)
            trans_reshaped *= np.hstack((offset_table[:half_period], offset_table[half_period - 1::-1]))
            trans_reshaped += np.roll(np.arange(-half_period, half_period), half_period)

            table[trans_table] += table[offset(length):offset(length + 1)]

    return ret


index, length = solve()
print(format(index, "020b")[20 - length:])
