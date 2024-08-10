def bug_hunt(program):
    lines = program.split(".\n")
    for line_number, line in enumerate(lines, 1):
        declarations = {}
        assigned = set()
        for l in line.split("\n"):
            if "[" in l:
                array_name, length = l.split("[")
                declarations[array_name] = int(length[:-1])
            elif "=" in l:
                left, right = l.split("=")
                array_name = left.split("[")[0]
                index = int("".join([c for c in left if c.isdigit()]))
                if index >= declarations[array_name] or array_name not in assigned:
                    return line_number
                assigned.add(array_name)
    return 0

# Sample Input
print(bug_hunt("a[3]\na[0]=a[1]\n.\nx[1]\nx[0]=x[0]\n.\na[0]\na[0]=1\n.\nb[2]\nb[0]=2\nb[1]=b[b[0]]\nb[0]=b[1]\n.\ng[2]\nG[10]\ng[0]=0\ng[1]=G[0]\n.\na[2147483647]\na[0]=1\nB[2]\nB[a[0]]=2\na[B[a[0]]]=3\na[2147483646]=a[2]\n.\n."))