import math

def rational(n, d):
    g = math.gcd(n, d)
    return [n//g, d//g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx*dy + ny*dx, dx*dy)

def mul_rationals(x,y):
    return (numer(x)*numer(y), denom(x), denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

half = rational(3,6)
print_rational(half)
