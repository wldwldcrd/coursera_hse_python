def MinDivisor(n):
    i = 2
    while (i <= int(n ** 0.5)):
        if not (n % i):
            return i
        i += 1
    return n


n = int(input())
print(MinDivisor(n))
