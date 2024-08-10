class Matrix():
    mod=10**9+7

    def set_mod(m):
        Matrix.mod=m

    def __init__(self,L):
        self.row=len(L)
        self.column=len(L[0])
        self._matrix=L
        for i in range(self.row):
            for j in range(self.column):
                self._matrix[i][j]%=Matrix.mod

    def __getitem__(self,item):
        if type(item)==int:
            raise IndexError("you must specific row and column")
        elif len(item)!=2:
            raise IndexError("you must specific row and column")

        i,j=item
        return self._matrix[i][j]

    def __setitem__(self,item,val):
        if type(item)==int:
            raise IndexError("you must specific row and column")
        elif len(item)!=2:
            raise IndexError("you must specific row and column")

        i,j=item
        self._matrix[i][j]=val

    def __add__(self,other):
        if (self.row,self.column)!=(other.row,other.column):
            raise SizeError("sizes of matrixes are different")

        res=[[0 for j in range(self.column)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):
                res[i][j]=self._matrix[i][j]+other._matrix[i][j]
                res[i][j]%=Matrix.mod
        return Matrix(res)

    def __mul__(self,other):
        if type(other)!=int:
            if self.column!=other.row:
                raise SizeError("sizes of matrixes are different")

            res=[[0 for j in range(other.column)] for i in range(self.row)]
            for i in range(self.row):
                for j in range(other.column):
                    temp=0
                    for k in range(self.column):
                        temp+=self._matrix[i][k]*other._matrix[k][j]
                    res[i][j]=temp%Matrix.mod
            return Matrix(res)
        else:
            n=other
            res=[[(n*self._matrix[i][j])%Matrix.mod for j in range(self.column)] for i in range(self.row)]
            return Matrix(res)

    def __pow__(self,m):
        if self.column!=self.row:
            raise MatrixPowError("the size of row must be the same as that of column")

        n=self.row
        res=Matrix([[int(i==j) for i in range(n)] for j in range(n)])
        while m:
            if m%2==1:
                res=res*self
            self=self*self
            m//=2
        return res

    def __str__(self):
        res=[]
        for i in range(self.row):
            for j in range(self.column):
                res.append(str(self._matrix[i][j]))
                res.append(" ")
            res.append("\n")
        res=res[:len(res)-1]
        return "".join(res)

N,M=map(int,input().split())
X=list(map(int,input().split()))+[N]
dp=[0]*(M+2)
dp[0]=1
A=Matrix([[4,-2,1],[1,0,0],[0,1,0]])
DP=Matrix([[0],[0],[0]])
first=0
base=Matrix([[5],[1],[0]])

for i in range(1,M+2):
    DP=(A**(X[i-1]-first))*(DP+base*(-dp[i-1]))
    dp[i]=DP[2,0]
    first=X[i-1]

print((-dp[-1])%(10**9+7))