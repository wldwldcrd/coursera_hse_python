def ReduceFraction(n, m):
    i = 2
    p = n
    q = m
    while i <= min(n, m):
        if not (n % i) and not (m % i):
            [p, q] = ReduceFraction(n // i, m // i)
            return p, q
        i += 1
    return p, q


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
