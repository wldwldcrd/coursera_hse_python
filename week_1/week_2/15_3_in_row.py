(a, b, c) = (int(input()), int(input()), int(input()))

if (a < b):
    (a, b) = (b, a)
if (a < c):
    (a, c) = (c, a)
if (b < c):
    (b, c) = (c, b)
print(c, b, a)
