def fibonacci(n) :
    """Return the sum of the first n natural numbers.

    >>> fibonacci(8)
    12
    >>> fibonacci(2)
    1
    """

    pred, curr = 0, 1
    k = 2
    while(k < n) :
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

result = fibonacci(8)
print(result)