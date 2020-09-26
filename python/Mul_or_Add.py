#p.312 곱하기 혹은 더하기

#여러개의 숫자로 구성된 하나의 문자열 리스트에 원소별로 각각 담기
input_s = str(input())
s = []
for i in range(len(input_s)):
    s.append(int(input_s[i]))

def mul_add(s):
    result = 0
    #차례차례 계산
    for value in s:
        if result == 0:
            result += value
            continue
        if value == 0:
            result += value
            continue
        result *= value
    return result

print(mul_add(s))
        
