inf = 10**10
def sg_func(a,b):
    res = [0,0,0]
    if(a[2]==0):
        res[0] = min(a[0],b[0])
        res[1] = min(a[1],b[1])
    else:
        res[0] = min(a[0],b[1])
        res[1] = min(a[1],b[0])

    res[2] = (a[2]+b[2])%2

    return res


class Seg_cus():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = inf
        self.func = sg_func

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [[self.ide_ele_min,self.ide_ele_min,0] for _  in range(2*self.num_max)]

        for i,num in enumerate(x, self.num_max):
            self.x[i][0] = num
            self.x[i][2] = 1
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def delete(self,i):
        i += self.num_max
        self.x[i][0] = inf
        self.x[i][2] = 0
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = [self.ide_ele_min,self.ide_ele_min,0]
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        stack_i = []
        stack_j = []
        while(i<=j):
            if(i==j):
                stack_i.append(i)
                break
            if(i&1):
                stack_i.append(i)
                i += 1
            if(not j&1):
                stack_j.append(j)
                j -= 1
            i = i>>1
            j = j>>1
        for i in stack_i:
            res = self.func(res,self.x[i])
        for i in stack_j[::-1]:
            res = self.func(res,self.x[i])

        return res

class Seg_min():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**10
        self.func = min

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele_min]*2*self.num_max

        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def update(self,i,x):
        i += self.num_max
        self.x[i] = x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele_min
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                res = self.func(res,self.x[i])
                break
            if(i&1):
                res = self.func(res,self.x[i])
                i += 1
            if(not j&1):
                res = self.func(res,self.x[j])
                j -= 1
            i = i>>1
            j = j>>1
        return res

n = int(input())
p = list(map(int,input().split()))

ind = [0] * (n+1)
for i,pi in enumerate(p):
    ind[pi] = i

st = Seg_cus(p)
st_ind = Seg_min([n] * n)

ans = []
for _ in range(n//2):
    num1 = st.query(0,n)[0]
    num2 = st.query(ind[num1],st_ind.query(ind[num1],n))[1]
    ans.append(num1)
    ans.append(num2)

    # print(num1,num2)
    # print(ind[num1],ind[num2])
    # print(st.x)
    # print(st_ind.x)
    st.delete(ind[num1])
    st.delete(ind[num2])
    st_ind.update(ind[num1],ind[num1])
    st_ind.update(ind[num2],ind[num2])

print(' '.join(map(str,ans)))