max_0 = max_1 = 0
act = int(input())
while act != 0:
    if act > max_0:
        (max_0, max_1) = (act, max_0)
    elif act > max_1:
        max_1 = act
    act = int(input())
print(max_1)
