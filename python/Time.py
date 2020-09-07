#p.113 시각

#시각 입력
N = int(input())

#갯수를 셀 변수
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):     #if 문 쓰는 요령 알아두기!
                count += 1

print(count)
