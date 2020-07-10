a = input()

first = a.find('f')
second = a.find('f', first + 1)
if first == -1:
    print(-2)
else:
    print(second)
