a = input()

first = a.find('h')
last = a.rfind('h')
print(a[:first] + a[last + 1:])
