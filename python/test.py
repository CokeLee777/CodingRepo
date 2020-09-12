array1 = [5,7,9,0,3,1,6,2,4,8]

def quick_sort1(array1):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array1) <= 1:
        return array1

    pivot = array1[0]   #피벗
    tail = array1[1:]   #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort1(left_side) + [pivot] + quick_sort1(right_side)


