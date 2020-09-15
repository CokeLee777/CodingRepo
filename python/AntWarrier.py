#p.220 개미전사

#식량창고의 갯수 입력
N = int(input())

#각 식량창고에 저장된 식량의 갯수 입력
K = list(map(int, input().split()))

#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*100

#다이나믹 프로그래밍 진행 (보텀업)
d[0] = K[0]
d[1] = max(K[0], K[1])
for i in range(2,N):
    d[i] = max(d[i-1], d[i-2] + K[i])

print(d[N-1])