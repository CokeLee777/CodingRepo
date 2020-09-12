#p.180 성적이 낮은 순서로 학생 출력하기

#학생의 수 입력
N = int(input())

#학생 이름과 성적 리스트 생성
arr = []
for i in range(N):
    input_data = input().split()
    #이름과 점수 튜플에 담아서 리스트에 저장
    arr.append((input_data[0],int(input_data[1])))

arr = sorted(arr, key=lambda student: student[1]) 

for student in arr:
    print(student[0], end=' ')
    