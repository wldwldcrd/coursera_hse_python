def IsPrime(n):
    i = 2
    while (i <= n // i):
        if not (n % i):
            return 'NO'
        i += 1
    return 'YES'


n = int(input())
print(IsPrime(n))
