x = int(input())
max_in_row = x
while x != 0:
    if (max_in_row < x):
        max_in_row = x
    x = int(input())
print(max_in_row)
