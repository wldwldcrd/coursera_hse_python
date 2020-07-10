e = 10 ** (-2)
a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c
if (0 <= d) and (d < e):
    print('{0:.10f}'.format(-b / (2 * a)))
elif d >= e:
    if a >= 0:
        print("{0:.10f} {1:.10f}".format(((-b - d ** 0.5) / (2 * a)),
                                         ((-b + d ** 0.5) / (2 * a))))
    else:
        print("{0:.10f} {1:.10f}".format(((-b + d ** 0.5) / (2 * a)),
                                         ((-b - d ** 0.5) / (2 * a))))
