numList = list(map(int, input().split()))
min_val = 1001
for act_val in numList:
    if 0 < act_val < min_val:
        min_val = act_val
print(min_val)
