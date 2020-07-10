p = int(input())
x = int(input())
y = int(input())

res = ((100 * x + y) * (100 + p)) // 100
print(res // 100, res % 100)
