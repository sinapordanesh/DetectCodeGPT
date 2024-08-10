import string
import sys


def main():
    str1 = sys.stdin.read()
    dict1 = {}
    for char in str1.lower():
        if not char.isalpha():
            continue
        elif dict1.__contains__(char):
            dict1[char] += 1
        else:
            dict1[char] = 1
    for char in string.ascii_lowercase:
        print(char + ' : ' + (str(dict1[char]) if dict1.__contains__(char) else '0'))


if __name__ == '__main__':
    main()

