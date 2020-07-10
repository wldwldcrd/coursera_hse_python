even_num = 0
act = int(input())
while act != 0:
    even_num += (1 - act % 2)
    act = int(input())
print(even_num)
