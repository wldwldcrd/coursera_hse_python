def CountSort(a):
    count = [0] * 101
    for i in a:
        count[i] += 1
    a = []
    for i in range(0, 101):
        for j in range(count[i]):
            a.append(i)
    return a


a = list(map(int, input().split()))
print(*CountSort(a))
