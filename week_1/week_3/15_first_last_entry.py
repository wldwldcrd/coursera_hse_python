a = input()

first = a.find('f')
last = a.rfind('f')
if first != -1:
    if first == last:
        print(first)
    else:
        print(first, last)
