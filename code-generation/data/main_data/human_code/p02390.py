import sys


def main():
    sec = int(sys.stdin.readline())
    hour = int(sec / 3600)
    sec = sec % 3600
    minute = int(sec / 60)
    sec = sec % 60
    print("{0}:{1}:{2}".format(hour,minute,sec))
    return


if __name__ == '__main__':
    main()

