inFile = open('input.txt', 'r', encoding='utf8')

countDict = {}
for line in inFile:
    tempData = line.strip().split()
    for word in tempData:
        countDict[word] = countDict.get(word, -1) + 1
        print(countDict[word], end=' ')

# print(countDict)

inFile.close()
