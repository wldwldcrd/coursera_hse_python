numList = list(map(float, input().split()))
num_of_pos = 0
for item in numList:
    if item > 0:
        num_of_pos += 1
print(num_of_pos)
