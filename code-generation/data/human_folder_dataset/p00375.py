def to_cels(f):
    return (f-30)/2
while True:
    try:
        f=int(input())
        print(int(to_cels(f)))
    except:
        break
