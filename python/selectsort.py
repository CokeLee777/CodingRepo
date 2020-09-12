#선택정렬 알고리즘

#임의의 리스트 생성
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
		#최소값이 들어있는 인덱스를 임의로 맨앞부터 선정
    min_index = i
		#두 번째 인덱스부터 비교
    for j in range(i+1, len(array)):
		#해당 인덱스의 값이 임의로 정한 최소값의 인덱스보다 크다면 최소값의 인덱스를 변경  
        if array[j] < array[min_index]:
            min_index = j
		#최소값을 제일 첫번째 인덱스부터 바꾸면서 채워나간다.
    array[i], array[min_index] = array[min_index], array[i] #스와프

print(array)
