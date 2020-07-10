n = int(input())
i = 2
while i < n:
    if not (n % i):
        break
    i += 1
print(i)
