def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f

def pow(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product* x, k + 1
    return product

pow_curried = curry2(pow)
print(pow_curried(2)(5))
