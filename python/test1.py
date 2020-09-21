#공간의 크기 입력받기
n = int(input())
#여행가가 이동할 계획서 내용을 입력받기
plan_data = list(map(str, input().split()))

start = (0,0)
#이동 반경 리스트 만들기
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(len(plan_data)):
    if plan_data[i] == 'U':

    elif plan_data[i] == 'D':

    elif plan_data[i] == 'L':

    elif plan_data[i] == 'R':

    