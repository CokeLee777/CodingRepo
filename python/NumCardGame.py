#p.96 숫자 카드게임
#행 과 열을 공백을 기준으로 입력받는다.
n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #가장 작은 수 중에서 가장 큰 수 찾기
    result = max(result, min_value) #result 와 min_value 중에 큰수를 result 에 대입한다.

print(result)