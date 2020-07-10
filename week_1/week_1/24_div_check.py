a = int(input())
b = int(input())
is_div = 1 - ((a % b) + b - 1) // b
print('YES' * is_div, 'NO' * (1 - is_div), sep='')
