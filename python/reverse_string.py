#p.313 문자열 뒤집기
input_s = str(input())
s = []
for i in range(len(input_s)):
    s.append(input_s[i])
    #마지막 횟수를 더하기 위한 연산
    if i == len(input_s)-1 and s[i] == '0':
        s.append('1')
        continue
    if i == len(input_s)-1 and s[i] == '1':
        s.append('0')
        continue
#뒤집는 횟수 초기화
reverse_cnt = 0
#0과1의 처음 갯수 담기
z_cnt = s.count('0')
o_cnt = s.count('1')
#원소의 갯수가 많은 값 변수에 담기
if z_cnt > o_cnt:
    max_value = '0'
else:
    max_value = '1'

for x,y in zip(s,s[1:]):
    if str(x) == str(y):
        continue
    if str(x) != str(y) and str(y) != max_value:
        continue
    if str(x) != str(y) and str(y) == max_value:
        reverse_cnt += 1
    
print(reverse_cnt)