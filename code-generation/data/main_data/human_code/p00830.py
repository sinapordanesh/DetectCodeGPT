# from urllib.parse import urljoin

def testcase_ends():
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        return 1

    htmls = set(input() for i in range(n))
    files = set('/')
    for html in htmls:
        sp = html.split('/')
        for i in range(2, len(sp)):
            files.add('/'.join(sp[:i]) + '/')

        files.add(html)

    def find(url):
        has_ts = url.endswith('/')
        url = url.rstrip('/')
        sp = url.split('/')[1:]
        u = ['']
        for i, c in enumerate(sp, 1):
            if c == '..':
                if len(u) == 0: return None  # ???
                u.pop()
            elif c == '.':
                pass
            else:
                u.append(c)

            if ('/'.join(u) + '/') not in files:
                if i < len(sp):
                    return None
        else:
            u = '/'.join(u)

        if u.endswith('/') and (u+'index.html') in files:
            return u+'index.html'

        if (u+'/index.html') in files:
            return u+'/index.html'

        if u in files and not has_ts:
            return u

        return None

    for i in range(m):
        p1 = input()
        p2 = input()

        p1 = find(p1)
        p2 = find(p2)

        if p1 is None or p2 is None:
            print('not found')
        elif p1 == p2:
            print('yes')
        else:
            print('no')

def main():
    while not testcase_ends():
        pass

if __name__ == '__main__':
    main()

