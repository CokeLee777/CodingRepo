#p.314 만들 수 없는 금액

#가지고있는 동전의 갯수 입력받기
n = int(input())
#가지고있는 동전들 입력받기
coins = list(map(int, input().split()))
#동전들 정렬하기(오름차순)
coins.sort()

d = [0]*1000000
#0은 만들수 있다고 임의로 가정
d[0] = 1
d[1] = 0
#동전들중 1원이 있다면
if 1 in coins:
    d[1] = 1

for i in range(2,sum(coins)+1):
    
    