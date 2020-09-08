#p.110 상하좌우

#공간의 크기 사용자지정
N = int(input())

#사용자가 이동할 계획서 지정
Plan = list(map(str, input().split()))

#사용자 출발위치
n = 1
m = 1

for i in range(len(Plan)):
    if Plan[i] == 'L':
        if m != 1:
            m -= 1
    elif Plan[i] == 'R':
        if m != 5:
            m += 1
    elif Plan[i] == 'U':
        if n != 1:
            n -= 1
    elif Plan[i] == 'D':
        if n != 5:
            n += 1

print(n,m)