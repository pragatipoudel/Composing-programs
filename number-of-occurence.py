def count(s, value):
    total = 0
    for i in s:
        if i == value:
            total += 1;
    return total

s = [1, 8, 2, 8]
result = count(s, 8)
print(result)