list_size = int(input())
numList = list(map(int, input().split()))
target_value = int(input())
difference = abs(target_value - numList[0])
result = numList[0]
for act_val in numList:
    if (abs(act_val - target_value) < difference):
        difference = abs(act_val - target_value)
        result = act_val
print(result)
