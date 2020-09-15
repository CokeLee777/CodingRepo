#p.217 1로 만들기

result = 0
#함수 생성
def to1(x, result):
    result += 1
    if x % 5 == 0:
        return to1(x // 5, result)
    elif x % 3 == 0:
        return to1(x // 3, result)
    elif x % 2 == 0:
        return to1(x // 2, result)
    elif x != 1:
        return to1(x - 1, result)
    else:
        return result

input_num = int(input())
print(to1(input_num, result))