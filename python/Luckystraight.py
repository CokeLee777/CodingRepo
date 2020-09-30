#p.321 럭키 스트레이트

#점수 입력받기
n = list(map(int, input().split()))
#중간지점구하기
first = 0
end = len(n)
mid = (first+end)//2

sum_left = 0
sum_right = 0
for i in range(first,mid):
    sum_left += n[i]
for j in range(mid,end):
    sum_right += n[j]

if sum_left == sum_right:
    print('LUCKY')
else:
    print('READY')