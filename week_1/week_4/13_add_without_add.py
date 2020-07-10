def sum(a, b):
    if b > 0:
        return 1 + sum(a, b - 1)
    return a


a = int(input())
b = int(input())
print(sum(a, b))
