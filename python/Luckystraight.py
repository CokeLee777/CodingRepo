#p.321 럭키 스트레이트

#점수 입력받기
n = list(map(int, input()))
#중간지점구하기
first = 0
end = len(n)
mid = (first+end)//2

sum_left = []
sum_right = []

for i in range(len(n)):
    if i < mid:
        sum_left.append(n[i])
    else:
        sum_right.append(n[i])

if sum(sum_left) == sum(sum_right):
    print('LUCKY')
else:
    print('READY')