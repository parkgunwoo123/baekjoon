counts, weight =  input().split()
list = []
tmpList = []
for count in range(0, int(counts)):
    tmp1, tmp2 = input().split()
    list.append([int(tmp1), int(tmp2)])

for ct in range(0, int(counts) + 1):
    max = 0
    tmpList.append([])
    for val in range(0, int(weight) + 1):
        if ct < 1:
            tmpList[ct].append(0)
        elif list[ct - 1][0] > val:
            tmpList[ct].append(tmpList[ct - 1][val])
    
        elif tmpList[ct - 1][val] >= tmpList[ct - 1][val - list[ct - 1][0]] + list[ct - 1][1]:
            tmpList[ct].append(tmpList[ct-1][val])
    
        else:
            tmpList[ct].append(tmpList[ct - 1][val -list[ct - 1][0]] + list[ct - 1][1])
    

print(tmpList[int(counts)][int(weight)])
