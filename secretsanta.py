import random

NameList = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']

if len(NameList)%2:
    print("list is odd. Input even number of names.")

NameList.append('Name6')

ShuffledNameList = []

while len(NameList) > 1:
    randNum = random.randrange(0,len(NameList)-1)
    ShuffledNameList.append(NameList[randNum])
    NameList.pop(randNum)

# add remaining name
ShuffledNameList.append(NameList[0])

SecretSanta = []

for i in range(0,len(ShuffledNameList),2):
    SecretSanta.append([ShuffledNameList[i],ShuffledNameList[i+1]])

print(SecretSanta)