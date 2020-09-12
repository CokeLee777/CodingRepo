#삽입 정렬

#임의의 리스트 생성
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    #i부터 0까지 -1 씩 감소하며 반복
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]

print(array)