# -*- coding: utf-8 -*-

# pandas 불러오기 (pandas 시리즈의 약칭을 pd 라고 붙힌다.)
import pandas as pd


# key:value 쌍으로 사전을 만들고, 변수 dict_data 에 저장
dict_data = {'a':1, 'b':2, 'c':3}

#판다스 Series 함수로 사전을 Series 로 변환. 변수 sr에 저장
sr = pd.Series(dict_data)

#sr 의 자료형 출력
print(type(sr))
print('\n')

#변수 sr에 저장되어있는 시리즈 객체를 출력한다.
print(sr)
