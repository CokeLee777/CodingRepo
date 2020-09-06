# -*- coding: utf-8 -*-

import pandas as pd

#IPython 디스플에이 설정 변경
pd.set_option('display.max_columns', 10)    #출력할 최대 열의 갯수
pd.set_option('display.max_colwidth', 20)   #출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True) #유니코드 사용 너비 조정

#주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('./stock price.xlsx')
df2 = pd.read_excel('./stock valuation.xlsx')

print(df1, '\n')
print(df2, '\n')

#데이터프레임 합치기 -교집합
#merge 는 on=None 옵션과 how='inner'옵션이 기본값
merge_inner = pd.merge(df1,df2)
print(merge_inner, '\n')

#데이터프레임 합치기 -합집합
merge_outer = pd.merge(df1,df2, how='outer', on='id')   #id열을 행인덱스로 지정
print(merge_outer, '\n')

#데이터프레임 합치기 -왼쪽 데이터프레임 기준, 키값 분리
merge_left = pd.merge(df1,df2, how='left', left_on='stock_name', right_on='name')
print(merge_left, '\n')

#데이터프레임 합치기 -오른쪽 데이터프레임 기준, 키 값 분리
merge_right = pd.merge(df1,df2, how='right', left_on='stock_name', right_on='name')
print(merge_right, '\n')

#불린 인덱싱과 결합하여 원하는 데이터 찾기
price = df1[df1['price'] < 50000]
print(price.head())
