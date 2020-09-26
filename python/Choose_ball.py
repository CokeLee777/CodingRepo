#p.315 볼링공 고르기

#볼링공의 갯수, 최대 볼링공의 무게 입력받기
n,m = map(int, input().split())
#각 볼링공의 무게 입력받기
k = list(map(int, input().split()))
#결과값 초기화
result = 0

for i in range(n-1):
    for j in range(i+1,n):
        if k[i] != k[j]:
            result += 1

print(result)       
