#p.311 모험가 길드

#모험가의 수 입력받기
n = int(input())
#각 모험가의 공포도의 값 입력받기
scary = list(map(int, input().split()))
scary.sort()

count = 0
#함수구현
def guild(n,scary,count):
    #공포도를 오름차순으로 정렬
    if n <= 0:
        return count
    max_scary = scary[n-1]
    n -= max_scary
    count += 1
    return guild(n,scary[:n],count)

print(guild(n,scary,count))