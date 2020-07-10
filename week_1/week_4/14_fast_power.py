def req_power(a, n):
    if n % 2:
        if n == 1:
            return a
        return a * req_power(a, n - 1)
    else:
        if n == 0:
            return 1
        return req_power(a ** 2, n / 2)


a = float(input())
n = int(input())
print(req_power(a, n))
