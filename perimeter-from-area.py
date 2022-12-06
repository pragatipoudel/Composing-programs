def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

area = 80
print(minimum_perimeter(area))
