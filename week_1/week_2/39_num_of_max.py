max_0 = 0
num_of_max = 1
act = int(input())
while act != 0:
    if act > max_0:
        max_0 = act
        num_of_max = 1
    elif act == max_0:
        num_of_max += 1
    act = int(input())
print(num_of_max)
