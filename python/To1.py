#p.99 1이 될때 까지

#N과 K 를 입력받는다.
N,K = map(int, input().split())

result = 0

#N이 1이 될 때 까지 반복
while N != 1:
    if N % K != 0:
        N -= 1
        result += 1
    elif N % K == 0:
        N = N / K
        result += 1

print(result)
