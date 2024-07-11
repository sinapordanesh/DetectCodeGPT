class Mint:
    MOD = 1000000007  # Must be a prime
    CACHE_FACTORIALS = [1, 1]
 
    def __init__(self, v):
        if self.__isally(v):
            self.v = v.v
        else:
            self.v = v % self.MOD
 
    @property
    def inv(self):
        return Mint(self.__minv(self.v))
 
    @classmethod
    def factorial(cls, v):
        for i in range(len(cls.CACHE_FACTORIALS), int(v) + 1):
            cls.CACHE_FACTORIALS.append(cls.CACHE_FACTORIALS[-1] * i % cls.MOD)
        return Mint(cls.CACHE_FACTORIALS[int(v)])
 
    @classmethod
    def perm(cls, n, r):
        if n < r or r < 0:
            return 0
        return cls.factorial(n) // cls.factorial(n - r)
 
    @classmethod
    def comb(cls, n, r):
        if n < r or r < 0:
            return 0
        return cls.perm(n, r) // cls.factorial(r)
 
    @classmethod
    def __isally(cls, v) -> bool:
        return isinstance(v, cls)
 
    @classmethod
    def __minv(cls, v) -> int:
        return pow(v, cls.MOD - 2, cls.MOD)
 
    @classmethod
    def __mpow(cls, v, w) -> int:
        return pow(v, w, cls.MOD)
 
    def __str__(self):
        return str(self.v)
    __repr__ = __str__
 
    def __int__(self):
        return self.v
 
    def __eq__(self, w):
        return self.v == w.v if self.__isally(w) else self.v == w
 
    def __add__(self, w):
        return Mint(self.v + w.v) if self.__isally(w) else Mint(self.v + w)
    __radd__ = __add__
 
    def __sub__(self, w):
        return Mint(self.v - w.v) if self.__isally(w) else Mint(self.v - w)
 
    def __rsub__(self, u):
        return Mint(u.v - self.v) if self.__isally(u) else Mint(u - self.v)
 
    def __mul__(self, w):
        return Mint(self.v * w.v) if self.__isally(w) else Mint(self.v * w)
    __rmul__ = __mul__
 
    def __floordiv__(self, w):
        return Mint(self.v * self.__minv(w.v)) if self.__isally(w) else Mint(self.v * self.__minv(w))
 
    def __rfloordiv__(self, u):
        return Mint(u.v * self.__minv(self.v)) if self.__isally(u) else Mint(u * self.__minv(self.v))
 
    def __pow__(self, w):
        return Mint(self.__mpow(self.v, w.v)) if self.__isally(w) else Mint(self.__mpow(self.v, w))
 
    def __rpow__(self, u):
        return Mint(self.__mpow(u.v, self.v)) if self.__isally(u) else Mint(self.__mpow(u, self.v))

n, k = map(int,input().split())    
for i in range(1, k+1):
    print(Mint.comb(n-k+1, i) * Mint.comb(k-1, i-1))