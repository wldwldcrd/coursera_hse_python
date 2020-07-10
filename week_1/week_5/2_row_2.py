a = int(input())
b = int(input())

if a <= b:
    step = 1
else:
    step = -1

for item in tuple(range(a, b + step, step)):
    print(item, end=' ')
print()
