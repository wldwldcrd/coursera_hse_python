numList = list(map(int, input().split()))

for item in numList:
    if not (item % 2):
        print(item, end=' ')

print()
