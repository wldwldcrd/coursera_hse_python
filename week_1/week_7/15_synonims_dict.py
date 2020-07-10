inFile = open('input.txt', 'r', encoding='utf8')

n = int(inFile.readline())
synDict = {}
for i in range(n):
    line = list(inFile.readline().strip().split())
    synDict[line[0]] = line[1]
    synDict[line[1]] = line[0]
print(synDict[inFile.readline().strip()])

inFile.close()
