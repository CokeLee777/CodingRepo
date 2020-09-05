# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('./stock-data.csv')

#데이터 내용 및 자료형 확인
print(df.head())
print('\n')
print(df.info())

#문자열 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date']) #df에 새로운 열로 추가

#데이터 내용 및 자료형 확인
print(df.head())
print('\n')
print(df.info())

#시계열 값으로 변환될 열을 새로운 행 인덱스로 지정, 기존날짜열은 삭제
df.set_index(['new_Date'], inplace=True)
df.drop('Date',axis=1,inplace=True)

print(df.head())