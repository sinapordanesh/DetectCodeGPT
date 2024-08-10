def check_web_pages(N, M, data):
    web_pages = data[:N]
    
    def normalize_path(path):
        components = path.split('/')
        stack = []
        
        for comp in components:
            if comp == '' or comp == '.':
                continue
            elif comp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(comp)
        
        return '/'.join(stack)
    
    for i in range(N, N + 2*M, 2):
        path1 = normalize_path(data[i])
        path2 = normalize_path(data[i+1])
        
        if path1 in web_pages and path2 in web_pages:
            if path1 == path2:
                print("yes")
            else:
                print("no")
        else:
            print("not found")

# Sample Input
check_web_pages(5, 6, [
    '/home/ACM/index.html',
    '/ICPC/index.html',
    '/ICPC/general.html',
    '/ICPC/japanese/index.html',
    '/ICPC/secret/confidential/2005/index.html',
    '/home/ACM/',
    '/home/ICPC/../ACM/',
    '/ICPC/secret/',
    '/ICPC/secret/index.html',
    '/ICPC',
    '/ICPC/../ICPC/index.html',
    '/ICPC',
    '/ICPC/general.html',
    '/ICPC/japanese/.././',
    '/ICPC/japanese/./../',
    '/home/ACM/index.html',
    '/home/ACM/index.html/',
    1,
    4,
    '/index.html/index.html',
    '/',
    '/index.html/index.html',
    '/index.html',
    '/index.html/index.html',
    '/..',
    '/index.html/../..',
    '/index.html/',
    '/index.html/index.html/..'
])