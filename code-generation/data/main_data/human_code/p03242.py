
url = "https://atcoder.jp//contests/abc111/tasks/abc111_a"

def main():
    s = input()
    print(s.translate(str.maketrans({'1': '9', '9': '1'})))
    
    
if __name__ == '__main__':
    main()

    