inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

result_set = set()
for line in inFile:
    tempData = line.strip().split()
    for word in tempData:
        result_set.add(word)

print(len(result_set))

inFile.close()
outFile.close()




# import sys
#
# print(len(set(sys.stdin.read().split())))

