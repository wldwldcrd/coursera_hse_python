def req_power(a, n):
    while (n > 1):
        return a * req_power(a, n - 1)
    if n == 0:
        return 1
    else:
        return a


a = float(input())
n = int(input())
print(req_power(a, n))
