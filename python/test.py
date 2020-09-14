#이진 탐색

#이진 탐색 재귀함수 구현
def binary_search(array, start, end, target):
    #탐색을 하다가 찾을 데이터가 없어서 start 가 end 를 넘어가면 None 리턴
    if start > end:
        return None
    #중간점 지정
    mid = (start + end) // 2
    
    if target < array[mid]:
        binary_search(array, start, mid - 1, target)
    elif target == array[mid]:
        return mid
    else:
        binary_search(array, mid + 1, end, target)
    

#원소의 갯수 n 과 찾고자 하는 문자열 입력 받기
n, target = map(int, input().split())

#전체 원소 입력
array = list(map(int, input().split()))

result = binary_search(array, 0, n-1, target)

if result == None:
    print('원소를 찾을 수 없습니다.')
else:
    print(result + 1)