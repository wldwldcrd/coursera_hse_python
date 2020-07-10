numList = list(map(int, input().split()))
prev_val = numList[0]
for act_val in numList:
    if act_val > prev_val:
        print(act_val, end=' ')
    prev_val = act_val
print()
