class Man:
    last_name = ''
    grade = 0


n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.last_name = tempManData[0]
    man.grade = int(tempManData[1])
    peopleList.append(man)
peopleList.sort(key=lambda man: (-man.grade))
for man in peopleList:
    print(man.last_name)
