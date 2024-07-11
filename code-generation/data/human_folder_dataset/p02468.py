import sys

MOD = 1000000007

def pow_mod(m, n):
    if n == 1:
        return m % MOD
    else:
        tmp = pow_mod(m, n / 2)
        if n % 2 == 0:
            return tmp * tmp % MOD
        else:
            return tmp * tmp * m % MOD
    
if __name__ == '__main__':
    line = sys.stdin.readline()
    m, n = line.split()
    m, n = int(m), int(n)
    
    sys.stdout.write(str(pow_mod(m, n)) + '\n')
        