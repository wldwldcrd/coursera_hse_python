import math

e = 10 ** (-2)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = (b * f - d * e) / (b * c - d * a)
if abs(b) < e:
    y = (f - c * x) / d
else:
    y = (e - a * x) / b
print("{0:.10f} {1:.10f}".format(x, y))
