x = int(input())
x = x % (24 * 60 * 60)
h = x // (60 * 60)
x = x % (60 * 60)
m = x // 60
s = x % 60
print("%d:%02d:%02d" % (h, m, s))
