(a, b, c) = (int(input()), int(input()), int(input()))
match = (a == b) + (b == c) + (c == a)
if (match == 1):
    print(2)
else:
    print(match)
