def is_quad(x, y):
    if (abs(x) <= 1) and (abs(y) <= 1):
        return 'YES'
    return 'NO'


x = float(input())
y = float(input())
print(is_quad(x, y))
