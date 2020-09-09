# -*- coding: utf-8 -*-
#열 분리
import pandas as pd

df = pd.read_excel('./주가데이터.xlsx')
print(df.head(), '\n')
print(df.dtypes, '\n')

#열 분리하기
df['연월일'] = df['연월일'].astype('str') #자료형을 문자열로 변경
dates = df['연월일'].str.split('-')
print(dates, '\n')

#분리된 정보를 각각 새로운 열에 담아 df에 추가하기
df['연'] = dates.str.get(0)  #dates 변수의 원소 리스트의 0번째 인덱스 값
df['월'] = dates.str.get(1)  #dates 변수의 원소 리스트의 1번째 인덱스 값
df['일'] = dates.str.get(2)  #dates 변수의 원소 리스트의 2번째 인덱스 값
print(df.head(), '\n')

