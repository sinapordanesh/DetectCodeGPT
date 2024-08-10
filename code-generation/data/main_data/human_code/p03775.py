#n, *d = map(int, open(0).read().split())
# dream dreamer erase eraser 
n=int(input())

def f(a,b):
    return max(len(str(a)),len(str(b)))
m=10000
for a in range(1,10**10):
    if n%a==0:
        m=min(f(a,n//a),m)
    if n<a or n//a<a:
        break
print(m)