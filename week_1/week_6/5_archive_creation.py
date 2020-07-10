S, n = list(map(int, input().split()))
numList = list()
for i in range(0, n):
    numList.append(int(input()))

numList.sort()
i = 0
num = 0
for i in range(0, len(numList)):
    S -= numList[i]
    if S >= 0:
        num += 1
    else:
        break
print(num)
