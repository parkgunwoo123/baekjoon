counts, weight =  input().split()
list = []
tmpList = []
for count in range(0, int(counts)):
    tmp1, tmp2 = input().split()
    list.append([int(tmp1), int(tmp2)]) #리스트에 무게 및 가치 삽입

for ct in range(0, int(counts) + 1):
    max = 0
    tmpList.append([])
    for val in range(0, int(weight) + 1): # 2차원 배열 counts수에 + 1을 더하는 이유는 아무것도 고르지 않았을 때의 i = 0 을 포함해서 계산하기 위해서
        if ct < 1:
            tmpList[ct].append(0) 
        elif list[ct - 1][0] > val:     #점화식 K[i, w] = max(K[i - 1, w], K[i - 1, w - wi(i일 때의 무게)] + val(가치)
            tmpList[ct].append(tmpList[ct - 1][val])
    
        elif tmpList[ct - 1][val] >= tmpList[ct - 1][val - list[ct - 1][0]] + list[ct - 1][1]:
            tmpList[ct].append(tmpList[ct-1][val])
    
        else:
            tmpList[ct].append(tmpList[ct - 1][val -list[ct - 1][0]] + list[ct - 1][1])
    

print(tmpList[int(counts)][int(weight)]) # 가장 끝단의 값이 원하는 가장 큰 value 값
