#p.178 위에서 아래로

#수열의 속해있는 수의 갯수 N
N = int(input())

#수열을 리스트로 담는다
arr = []
for i in range(N):
    arr.append(int(input()))

#내림차순으로 정렬
arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=' ')
