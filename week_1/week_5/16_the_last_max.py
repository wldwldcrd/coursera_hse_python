numList = list(map(int, input().split()))
max_val = 0
max_pos = 0
act_pos = 0
for act_val in numList:
    if act_val >= max_val:
        max_val = act_val
        max_pos = act_pos
    act_pos += 1
print(max_val, max_pos)
