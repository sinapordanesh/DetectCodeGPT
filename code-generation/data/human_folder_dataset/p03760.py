def answer(o: str, e: str) -> str:
    result = ''
    e += ' '
    for i in range(len(o)):
        result += o[i] + e[i]

    return result.strip()


def main():
    o = input()
    e = input()
    print(answer(o, e))


if __name__ == '__main__':
    main()