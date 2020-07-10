(a, b, c, d, e) = (int(input()), int(input()), int(input()),
                   int(input()), int(input()))
# sort brick
if (a < b):
    (a, b) = (b, a)
if (a < c):
    (a, c) = (c, a)
if (b < c):
    (b, c) = (c, b)
# sort hole
if (d < e):
    (d, e) = (e, d)
# check
if ((d >= b) and (e >= c)):
    print('YES')
else:
    print('NO')
