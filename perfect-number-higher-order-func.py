import operator

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
        reduced = initial
        for x in s:
            reduced = reduce_fn(reduced, x)
        return reduced

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return[1] + keep_if(divides_n, range(2, n))

def sum_of_divisors(n):
    return reduce(operator.add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

result = keep_if(perfect, range(1, 1000))
print(result)
