from collections import deque


def discard(c: str, da: deque, db: deque, dc: deque) -> str:
    if eval(f'len(d{c})'):
        c = eval(f'd{c}.popleft()')
    else:
        return c.upper()

    return discard(c, da, db, dc)


def answer(sa: str, sb: str, sc: str) -> str:
    deque_a = deque(list(sa))
    deque_b = deque(list(sb))
    deque_c = deque(list(sc))
    return discard(deque_a.popleft(), deque_a, deque_b, deque_c)


def main():
    sa, sb, sc = [input() for _ in range(3)]
    print(answer(sa, sb, sc))


if __name__ == '__main__':
    main()