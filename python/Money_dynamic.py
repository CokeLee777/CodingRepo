#p.226 효율적인 화폐구성

#화폐종류의 갯수, 화폐들의 합 입력
N, M = map(int, input().split())

#N개의 화폐 단위 입력
arr = []
for i in range(N):
    arr.append(int(input()))

#DP 테이블 초기화
d = [10001]*(M+1)

#다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
for i in range(N):
    #첫번째 화폐단위부터 화폐들의 합 까지 확인한다.
    for j in range(arr[i], M+1):
        if d[j-arr[i]] != 10001:    #(i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - arr[i]] + 1)

#계산된 결과 출력
#주어진 화폐단위로 만들지 못하면 -1 출력
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
