#p.182 두 배열의 원소 교체

#두 배열의 크기 N 과 바꿔치기 횟수 K 입력
N,k = map(int, input().split())
#두 배열 입력
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#A는 오름차순 정렬
A.sort()
#B는 내림차순 정렬
B = sorted(B, reverse=True)

for i in range(k):
    A[i], B[i] = B[i], A[i]


print(sum(A))