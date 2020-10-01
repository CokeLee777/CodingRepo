#p.322 문자열 재정렬

#문자열 s 입력받기
s = str(input())
#리스트 형태로 정렬값을 받음
s = sorted(s)

result = ""
num = 0
for string in s:
    if ord(string) >= 65:
        result += string
        continue
    num += int(string) 

result += str(num)

print(result)


