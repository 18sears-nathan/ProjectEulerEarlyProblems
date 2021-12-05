import random
import sys

# Problem 10
def twoMillPrimesSum(N):
    is_prime = [1]*N
    is_prime[0], is_prime[1] = 0, 0

    def sieve():
        i = 2
        while i*i <= N:
            if is_prime[i] == 0:
                i += 1
                continue
            j = 2*i
            while j < N:
                is_prime[j] = 0
                j += i
            i += 1
    sieve()
    sum = 0
    for i in range(1, N):
        if is_prime[i] == 1:
            print(i)
            sum += i
    print(sum)
   
# Problem 765
def trillionare():
    x0 = 1

    b = 1

    # Try many different proportions of b
    a = 1
    
    def trill(a, x0, b):
        ran = 5
        for i in range(0, 1000):
            # success, x = x+b
            if ran > 4:
                x0 = x0 + b
            else:
                x0 = x0 - b
            b = x0/a
            ran = random.randrange(1, 10)
        return (a, x0)
    
    returns = []
    for i in range(0, 100):
        returns.append(trill(a, x0, b))
        a = a + .01
    for r in returns:
        print(r)

# Problem 11
def adjprodgrid():
    grid = sys.stdin.readlines()
    fr = [str.split(line) for line in grid]
    fr = [[int(i) for i in line] for line in fr]

    prods = []
    for j in range(0, len(fr)):
        for i in range(0, len(fr)):
            # left
            if i-3 >= 0:
                prods.append((fr[j][i]*fr[j][i-1]*fr[j][i-2]*fr[j][i-3], i, j, "L", str(fr[j][i])))
            # right
            if i+3 < 20:
                prods.append((fr[j][i]*fr[j][i+1]*fr[j][i+2]*fr[j][i+3], i, j, "R", str(fr[j][i])))
            # down
            if j-3 >= 0:
                prods.append((fr[j][i]*fr[j-1][i]*fr[j-2][i]*fr[j-3][i], i, j, "D", str(fr[j][i])))
            # down
            if j+3 < 20:
                prods.append((fr[j][i]*fr[j+1][i]*fr[j+2][i]*fr[j+3][i], i, j, "U", str(fr[j][i])))
            # diag "/"
            if j+3 < 20 and i+3 < 20:
                prods.append((fr[j][i]*fr[j+1][i+1]*fr[j+2][i+2]*fr[j+3][i+3], i, j, "d1", str(fr[j][i])))
            # diag "/"
            if j-3 >= 0 and i-3 >= 0:
                prods.append((fr[j][i]*fr[j-1][i-1]*fr[j-2][i-2]*fr[j-3][i-3], i, j, "d2", str(fr[j][i])))
            # diag "\"
            if j+3 < 20 and i-3 >= 0:
                prods.append((fr[j][i]*fr[j+1][i-1]*fr[j+2][i-2]*fr[j+3][i-3], i, j, "d3", str(fr[j][i])))
            # diag "\"
            if j-3 >= 0 and i+3 < 20:
                prods.append((fr[j][i]*fr[j-1][i+1]*fr[j-2][i+2]*fr[j-3][i+3], i, j, "d4", str(fr[j][i])))
        
    print(len(prods))
    c = 0
    c1 = (-1, -1, -1, "-1")
    for i in range(0, len(prods)):
        if prods[i][0] > c:
            c = prods[i][0]
            c1 = prods[i]
    prods.sort()
    print(prods)
    print(c)
    print(c1)

# Problem 12 (attempt)
# def triangleDivs():
#     def tNum(n):
        
#         return int((n*(n+1))/2)

#     def factorCount(n):
#         f = [1]
#         d = 2
#         while d < n:
#             if 
        
        


 #   print(factorCount(tNum(7)))            

                
    
    # n = 500
    # while factorCount(tNum(n)) < 500:
    #     n += 1
    #     print("n, tNum(n), factors, = "+str(n)+", "+str(tNum(n))+", "+str(factorCount(tNum(n))))
    # return n
    
#print(triangleDivs())

# Extended Euclidian Algorithm
def ext_gcd(a, b):
    #(x, y) -> (old, new)
    p = (1, 0)
    q = (0, 1)
    r = (a, b)
    while r[1] != 0:
        j = r[0]//r[1]
        r = (r[1], r[0] - j*r[1])
        p = (p[1], p[0] - j*p[1])
        q = (q[1], q[0] - j*q[1])
    return (r[0], p[0], q[0])

# Fast modular inverse
def inv_mod(a, z):
    gcd, m, n = ext_gcd(a, z)
    if gcd != 1:
        raise ValueError
    else:
        return m % z

# Base 10 -> Base 2 (Fast?)
def b10tob2(x):
    r = ""
    while x >= 1:
        r = (('0' + r) if (x % 2) == 0 else ('1' + r))
        # Python integer division
        x = x//2
    return r

# Fast Modular Exponent
def EXP(a, n, p):
    r = 1
    n_bin = b10tob2(n)
    for i in range(0, len(str(n_bin))):
        r = (r * r) % p
        if n_bin[i] == "1":
            r = (r * a) % p
    return r

# Problem 16
def power_digit_sum():
    z = 2**1000
    z = str(z)
    print(z)
    sum = 0
    for c in z:
        sum += int(c)
    print(sum)

# Sieve of Eratosthenes (Find all primes below N)
def sieve(N):
    is_prime = [1]*N
    is_prime[0], is_prime[1] = 0, 0
    i = 2
    while i*i <= N:
        if is_prime[i] == 0:
            i += 1
            continue
        j = 2*i
        while j < N:
            is_prime[j] = 0
            j += i
        i += 1
    return(is_prime)

# Problem 773
def ruff(index):
    N = 1000
    p = sieve(N)
    p_ = []
    for i in range(0, len(p)):
        if p[i] == 1:
            p_.append(i)
    S_k = [2,5]
    counter = 0
    for n in p_:
        if n % 10 == 7 and counter < index:
            S_k.append(n)
            counter += 1
    print(S_k)

    def kruff(n):
        kr = True
        for s in S_k:
            if n % s == 0:
                kr = False
                break
        return kr
    for i in range(1,100):
        print(str(i)+" : "+str(kruff(i)))
    
    def prod_N_k(k):
        r = 1
        for i in range(0, k+1):
            r *= S_k[i]
        return r
    
    def F_k(k):
        N_k = prod_N_k(k)
        s = []
        element = 1
        while element < N_k:
            if kruff(element) and element % 10 == 7:
                s.append(element)
    print(F_k(index))
