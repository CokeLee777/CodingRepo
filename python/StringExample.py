#문자열 쓰는 방법
strvalue = ''' hello world '''
strvalue = """ hello world """

#문자열 다른줄에 이어쓰기
strvalue = '''hello     
world'''                    

#문자열 사이에 따옴표 넣기
strvalue = " 'hello world' "
strvalue = ' "hello world" '  
strvalue = " hello\' world" 

#문자열 줄바꿈
strvalue = "hello\nworld"   

#문자열 사이의 탭 간격
strvalue = "hello\tworld"   

#문자열 합,곱
strvalue = "hello"
print(strvalue + strvalue)
print(strvalue * 2)

#문자열 길이 구하기 (띄어쓰기도 포함)
strvalue = "hello world"
print(len(strvalue))

#문자열 인덱싱과 슬라이싱

#1.문자열 인덱싱
strvalue = "hello world"
#strvalue 의 0번째 항의 값을 표현한다.
print(strvalue[0]) 
#strvalue 의 -1번째 항은 d 이다
print(strvalue[-1])

#2. 문자열 슬라이싱
strvalue = "hello world"
#0번째항 부터 5번째항 직전까지 출력
print(strvalue[0:5]) #hello
#6번째항 부터 문자열의 끝까지 출력
print(strvalue[6:]) #world

#pithon 이라는 문자열을 python 으로 바꾸어 보자
sample = "pithon"
sample1 = sample[0]
sample2 = sample[2:]
sample = sample1 + "y" + sample2
print(sample)

#문자열 포매팅
#1. 숫자 바로 대입
print("I eat %d apples" %3)
#2. 문자열 바로 대입(%뒤에 큰따옴표나 작은따옴표 필수로 넣을것!)
print("I eat %s apples" %"five")
#3. 숫자 값을 나타내는 변수로 대입
num = 3
print("I eat %d apples" %num)
#4. 2개 이상의 값 넣기(%뒤에 괄호와 중간에 콤마로 구분)
num = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" %(num, day))


