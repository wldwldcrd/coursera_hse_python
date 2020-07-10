numList = list(map(int, input().split()))

min_val = numList[0]
min_pos = 0
max_val = numList[0]
max_pos = 0
act_pos = 0
for act_val in numList:
    if act_val < min_val:
        min_val = act_val
        min_pos = act_pos
    if act_val > max_val:
        max_val = act_val
        max_pos = act_pos
    act_pos += 1

numList[min_pos] = max_val
numList[max_pos] = min_val

print(*numList)
