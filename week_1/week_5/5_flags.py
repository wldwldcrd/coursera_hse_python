a = int(input())

for i in tuple(range(1, a + 1)):
    print('+___ ', end='')
print()
for i in tuple(range(1, a + 1)):
    print('|', i, ' / ', sep='', end='')
print()
for i in tuple(range(1, a + 1)):
    print('|__\ ', end='')
print()
for i in tuple(range(1, a + 1)):
    print('|    ', end='')
