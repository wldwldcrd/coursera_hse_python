a = input()

separator = a.find(' ')
print(a[separator + 1:] + ' ' + a[:separator])
