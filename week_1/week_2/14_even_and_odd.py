a = int(input())
b = int(input())
c = int(input())

if (a % 2 + b % 2 + c % 2) % 3:
    print('YES')
else:
    print('NO')
