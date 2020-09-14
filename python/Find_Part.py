#p.197 부품찾기

#이진 탐색 알고리즘 메서드 구현
def binary_search(array, target, start, end):
    #중간점 구축
    mid = (start + end) // 2

    #시작점이 끝점보다 커지면 찾는 원소가 리스트안에 없는 것 이므로 None 반환
    if start > end:
        return None
    
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] == target:
        return mid
    else:
        return binary_search(array, target, mid + 1, end)

#가게 부품 수를 입력받는다.
N = int(input())
#가게의 부품 수 만큼 부품 번호 입력
array = list(map(int, input().split()))
array.sort()
#손님이 찾는 부품 수 입력
M = int(input())
#손님이 찾는 부품 수 만큼 부품 번호 입력
target = list(map(int, input().split()))

for x in target:
    
    if binary_search(array, x, 0, N-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')



