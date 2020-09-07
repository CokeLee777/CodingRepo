#p.115 왕실의 나이트

#나이트 위치 입력받기
nPosition = str(input())
row = int(nPosition[1]) # 리스트가 아니어도 문자와 숫자가 섞여있는 문자열을 인덱싱할수 있다.
columns = int(ord(nPosition[0])) - int(ord('a')) + 1    #ord() 메서드는 유니코드문자의 정수형 번호를 불러온다.

#나이트가 이동할 수 있는 8가지 방향
steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

count = 0

for step in steps:
    next_row = row + step[0]
    next_columns = columns + step[1]

    if next_row >= 1 and next_row <= 8 and next_columns >= 1 and next_columns <= 8:
        count += 1

print(count)