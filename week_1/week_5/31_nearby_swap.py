numList = list(map(int, input().split()))
b = []
for i in range(0, len(numList), 2):
    if i < (len(numList) - 1):
        b.append(numList[i + 1])
    b.append(numList[i])
print(*b)
