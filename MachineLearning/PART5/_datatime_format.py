# -*- coding: utf-8 -*-
#날짜 데이터 분리
import pandas as pd

df = pd.read_csv('./stock-data.csv')

#문자열인 날짜 데이터를 판다스 Timestamp 로 변환
df['new_Date'] = pd.to_datetime(df['Date'])
print(df.head())
print('\n')

#dt속성을 이용하여 new_Date 열의 연-월-일 정보를 년,월,일로 구분
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day

print(df.head())

#Timestamp 를 Period 로 변환하여 연-월-일 표기 변경하기
df['Date_Yr'] = df['new_Date'].dt.to_period(freq='A')   #연도만 추출
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')    #년-월 추출

print(df.head())

#원하는 열을 새로운 행 인덱스로 지정
df.set_index('Date_m',inplace=True)
print(df.head())