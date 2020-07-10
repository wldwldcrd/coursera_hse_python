inFile = open('input.txt', 'r', encoding='utf8')

countDict = {}
for line in inFile:
    tempData = line.strip().split()
    for word in tempData:
        countDict[word] = countDict.get(word, 0) + 1

dictlist = []
for key, value in countDict.items():
    temp = [-value, key]
    dictlist.append(temp)
dictlist.sort()
for i in range(len(dictlist)):
    print(dictlist[i][1])

inFile.close()
