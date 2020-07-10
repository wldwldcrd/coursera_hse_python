a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
c = list()
while i < len(a) or j < len(b):
    if (i >= len(a)):
        c.append(b[j])
        j += 1
    elif (j >= len(b)):
        c.append(a[i])
        i += 1
    else:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

print(*c)
