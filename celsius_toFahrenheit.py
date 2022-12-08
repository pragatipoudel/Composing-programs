celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')

def converter(c, f):
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)

converter(celsius, fahrenheit)
celsius['set_val']('user', 25)
