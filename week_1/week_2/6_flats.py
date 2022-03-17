x = int(input())
y = int(input())

if (x - 1) % (y - x + 1):
    print('NO')
else:
    print('YES')
