#p.201 떡볶이 떡 만들기

#떡의 갯수와 요청한 떡의 길이 입력
N, M = map(int, input().split())
#떡의 각각의 높이 입력
array = list(map(int, input().split()))
array.sort()

#이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

#이진 탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        #잘랏을 때 떡의 양 계산
        if x > mid:
            total += x - mid
    #떡의 양이 부족한 경우 더 많이 자르기
    if total < M:
        end = mid - 1
    #떡의 양이 충분한 경우
    else:
        result = mid
        start = mid + 1

print(result)