def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        sum = fib(n-2) + fib(n-1)
        return sum

result = fib(6)
print(result)
