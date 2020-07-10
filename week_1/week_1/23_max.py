a = int(input())
b = int(input())
q = ((a - b) % 2001) // 1001
print(a * (1 - q) + b * q)
